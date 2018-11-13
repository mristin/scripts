#!/usr/bin/env python3

"""Bundle a Git repository to an archived file."""

import argparse
import pathlib
import shutil
import subprocess
import tempfile


def main() -> None:
    """"
    Main routine
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the repository", required=True)
    parser.add_argument("--target", help="path to the target file", required=True)
    args = parser.parse_args()

    assert isinstance(args.url, str)
    assert isinstance(args.target, str)

    url = args.url
    target = pathlib.Path(args.target)

    if subprocess.call(['which', 'git']) != 0:
        raise RuntimeError("git could not be found.")

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

        bundle_pth = repo_dir / "repo.bundle"

        target.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(src=bundle_pth.as_posix(), dst=target.as_posix())


if __name__ == "__main__":
    main()
