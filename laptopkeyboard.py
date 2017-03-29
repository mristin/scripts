#!/usr/bin/env python3
import subprocess
import re

from typing import Tuple


def main() -> None:
    """"
    Main routine
    """
    lines = subprocess.check_output(["xinput", "list"]).decode("utf-8").split("\n")

    id_re = re.compile(r'^.*id=(?P<id>[0-9]+).*\[slave +[a-z0-9_\-]+ +\((?P<master>[0-9]+)\)\]$')

    def extract(a_line: str) -> Tuple[str, str]:
        mtch = id_re.match(a_line)
        if mtch is None:
            raise RuntimeError('Unparsable line: {}'.format(repr(a_line)))
        return mtch.group("id"), mtch.group("master")

    touchpadid = touchpadmaster = ""
    keyboardid = keyboardmaster = ""
    for line in lines:
        if "Synaptics TouchPad" in line:
            touchpadid, touchpadmaster = extract(line)
        elif "AT Translated Set 2 keyboard" in line:
            keyboardid, keyboardmaster = extract(line)

    subprocess.check_call(["xinput", "float", touchpadid])
    subprocess.check_call(["xinput", "float", keyboardid])

    print("To enable:")
    print("xinput reattach {} {}".format(touchpadid, touchpadmaster))
    print("xinput reattach {} {}".format(keyboardid, keyboardmaster))


if __name__ == "__main__":
    main()
