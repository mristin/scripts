#!/usr/bin/env python3

"""Make a backup of all public Parquery repositories from github."""

import argparse
import concurrent.futures
import datetime
import json
import pathlib
import shutil
import subprocess
import tempfile
import threading
import uuid
from typing import List, Any

import requests


class Repo:
    """Represent a github repository."""

    def __init__(self, name: str, clone_url: str) -> None:
        self.name = name
        self.clone_url = clone_url


def repo_from_obj(obj: Any) -> List[Repo]:
    """Extract the repository information from the response parsed as JSON."""
    if not isinstance(obj, list):
        raise RuntimeError("Expected a list (JSON array), but got: {}".format(type(obj)))

    result = []  # type: List[Repo]
    for item in obj:
        if 'clone_url' not in item:
            raise RuntimeError("Expected a clone_url property in the item of the response: {!r}".format(item))

        if not isinstance(item['clone_url'], str):
            raise RuntimeError(
                "Expected a clone_url property as a string in the item of the response, but got: {!r}".format(
                    item['clone_url']))

        if 'name' not in item:
            raise RuntimeError("Expected a name property in the item of the response: {!r}".format(item))

        if not isinstance(item['name'], str):
            raise RuntimeError(
                "Expected a name property as a string in the item of the response, but got: {!r}".format(
                    item['name']))

        result.append(Repo(name=item['name'], clone_url=item['clone_url']))

    return result


def list_repos() -> List[Repo]:
    """List all repositories in the Parquery organization on github."""
    next_url = 'https://api.github.com/orgs/Parquery/repos?per_page=100'

    result = []  # type: List[Repo]

    while next_url is not None:
        resp = requests.get(next_url, timeout=30)
        assert isinstance(resp, requests.models.Response)

        if 'next' in resp.links:
            next_url = resp.links['next']['url']
        else:
            next_url = None

        obj = json.loads(resp.text)
        result.extend(repo_from_obj(obj=obj))

    return result


PRINT_LOCK = threading.Lock()


def bundle_repo(url: str, path: pathlib.Path) -> None:
    """Bundle the repository to the given path."""
    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = pathlib.Path(tmp_dir_str)
        subprocess.check_call(['git', 'clone', '--mirror', url], cwd=tmp_dir.as_posix())

        subpths = list(tmp_dir.iterdir())
        if len(subpths) != 1:
            raise RuntimeError("Expected only a single entry in {} after cloning the repo, but got: {}".format(
                tmp_dir, subpths))

        repo_dir = subpths[0]
        if not repo_dir.is_dir():
            raise RuntimeError("Expected the cloned directory to be a directory, but it's not: {}".format(repo_dir))

        subprocess.check_call(['git', 'bundle', 'create', 'repo.bundle', '--all'], cwd=repo_dir.as_posix())

        shutil.copy(src=(repo_dir / "repo.bundle").as_posix(), dst=path.as_posix())

        with PRINT_LOCK:
            print("Archived {} to {}.".format(url, path))


def main() -> None:
    """"Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target_dir", help="target directory where all snapshots of bundle files should reside",
                        required=True)
    args = parser.parse_args()

    target_dir = pathlib.Path(args.target_dir)

    if subprocess.call(['which', 'git'], stdout=subprocess.DEVNULL) != 0:
        raise RuntimeError("git could not be found.")

    now = datetime.datetime.utcnow()
    day_dir = target_dir / now.strftime("%Y-%m-%d")

    if day_dir.exists():
        print("The backup has been already performed for today: {}".format(day_dir))
        return

    tmp_day_dir = target_dir / "{}-{}".format(now.strftime("%Y-%m-%d"), uuid.uuid4())

    try:
        tmp_day_dir.mkdir(exist_ok=True)

        repos = list_repos()
        futures = []  # type: List[concurrent.futures.Future]
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            for repo in repos:
                bundle_pth = tmp_day_dir / "{}.bundle".format(repo.name)

                futures.append(executor.submit(bundle_repo, url=repo.clone_url, path=bundle_pth))

            for future in futures:
                future.result()

        tmp_day_dir.rename(day_dir)

    finally:
        if tmp_day_dir.exists():
            shutil.rmtree(tmp_day_dir.as_posix())

    ##
    # Keep only the last 30 days
    ##

    day_pths = sorted(target_dir.iterdir())
    morituri_day_pths = day_pths[:len(day_pths) - 30]
    for day_pth in morituri_day_pths:
        shutil.rmtree(day_pth.as_posix())


if __name__ == "__main__":
    main()
