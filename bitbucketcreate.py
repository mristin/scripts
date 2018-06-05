#!/usr/bin/env python3

""" creates a pull request on the bitbucket. """
import re
import subprocess
import sys


def main() -> int:
    """ executes the main routine. """
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], universal_newlines=True).strip()

    remote_origin = subprocess.check_output(
        ["git", "config", "--get", "remote.origin.url"], universal_newlines=True).strip()

    _, remote_origin = remote_origin.split("@")

    if remote_origin.startswith("bitbucket.org"):
        remote_origin = re.sub(r'\.git$', '', remote_origin)

        url = "https://{}/pull-requests/new?source={}&t=1".format(
            remote_origin, branch)

        subprocess.Popen(['firefox', url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    else:
        raise NotImplementedError("unhandled branch creation for the remote origin: {}".format(remote_origin))
    return 0


if __name__ == "__main__":
    sys.exit(main())
