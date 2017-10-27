#!/usr/bin/env python3
import subprocess
import tempfile
from typing import Dict

from pocketsphinx import LiveSpeech


def main() -> None:
    """"
    Main routine
    """
    original_path = 'venv/lib/python3.5/site-packages/pocketsphinx/model/cmudict-en-us.dict'

    words = [
        'may',
        'king',
        'sing',
        'semi',
        'switch',
        'minus',
        'score',
        'word',
        'shrink',
        'leg',
        'move',
        'parent',
        'bracket',
        'brag',
        'branch',
        'baseball',
        'carrot',
        'quote',
        'jump',
        'number',
        'page',
        'next',
        'copy',
        'paste',
        'home',
        'end',
        'document',
        'release',
        'conjunction',
        'alternation',
        'above',
        'down',
        'supervisor',
        'format',
        'find',
        'erase',
        'escape',
        'colon',
        'rename',
        'equals',
        'location',
        'search',
        'monkey',
        'confirm',
        'slash',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven'
    ]

    with tempfile.NamedTemporaryFile() as tmpdic:
        with open(original_path, 'rt', encoding='utf-8') as fid:
            lines = fid.readlines()

            line_map = {}  # type: Dict[str, str]
            for line in lines:
                parts=line.split(' ')
                word=parts[0].lower()

                line_map[word]=line

            for word in words:
                if not word.lower() in line_map:
                    raise KeyError("Word not found in {}: {}".format(original_path, word))

                tmpdic.file.write((line_map[word.lower()] + "\n").encode())
                tmpdic.file.flush()

        speech = LiveSpeech(dic=tmpdic.name)

        for phrase in speech:
            hyp = phrase.hypothesis()
            if hyp == "may":
                subprocess.check_call(["xdotool", "key", "Return"])
            elif hyp == "king" or hyp == "sing":
                subprocess.check_call(["xdotool", "key", "Tab"])
            elif hyp == "semi":
                subprocess.check_call(["xdotool", "key", "semicolon"])
            elif hyp == "switch":
                subprocess.check_call(["xdotool", "key", "Alt+Tab"])
            elif hyp == "minus":
                subprocess.check_call(["xdotool", "key", "minus"])
            elif hyp == "minus minus":
                subprocess.check_call(["xdotool", "key", "minus"])
                subprocess.check_call(["xdotool", "key", "minus"])
            elif hyp == "score":
                subprocess.check_call(["xdotool", "key", "underscore"])
            elif hyp == "word":
                subprocess.check_call(["xdotool", "key", "Ctrl+w"])
            elif hyp == "shrink":
                subprocess.check_call(["xdotool", "key", "Ctrl+Shift+w"])
            elif hyp == "leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "two leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "three leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "four leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "five leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "six leg":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "two move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "three move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "four move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "five move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "six move":
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Right"])
            elif hyp == "parent":
                subprocess.check_call(["xdotool", "key", "parenleft"])
            elif hyp == "curly":
                subprocess.check_call(["xdotool", "key", "braceleft"])
            elif hyp == "bracket":
                subprocess.check_call(["xdotool", "key", "bracketleft"])
            elif hyp == "brag":
                subprocess.check_call(["xdotool", "key", "bracketleft"])
            elif hyp == "branch":
                subprocess.check_call(["xdotool", "type", "gitbranch.py"])
            elif hyp == "status":
                subprocess.check_call(["xdotool", "type", "gitstatus.sh"])
            elif hyp == "create":
                subprocess.check_call(["xdotool", "type", "gitc.py"])
            elif hyp == "baseball":
                subprocess.check_call(["xdotool", "type", "git rebase -i master"])
            elif hyp == "carrot":
                subprocess.check_call(["xdotool", "type", "^"])
            elif hyp == "dollar":
                subprocess.check_call(["xdotool", "type", "$"])
            elif hyp == "quote":
                subprocess.check_call(["xdotool", "type", '"'])
            elif hyp == "quote quote quote":
                subprocess.check_call(["xdotool", "type", '"""'])
            elif hyp == "jump":
                subprocess.check_call(["xdotool", "key", "Ctrl+Shift+n"])
            elif hyp == "number":
                subprocess.check_call(["xdotool", "key", "Ctrl+g"])
            elif hyp == "page":
                subprocess.check_call(["xdotool", "key", "Prior"])
            elif hyp == "next":
                subprocess.check_call(["xdotool", "key", "Next"])
            # elif hyp == "cut":
            #    subprocess.check_call(["xdotool", "key", "Ctrl+x"])
            elif hyp == "copy":
                subprocess.check_call(["xdotool", "key", "Ctrl+c"])
            elif hyp == "paste":
                subprocess.check_call(["xdotool", "key", "Ctrl+v"])
            elif hyp == "home":
                subprocess.check_call(["xdotool", "key", "Home"])
            elif hyp == "end":
                subprocess.check_call(["xdotool", "key", "End"])
            # elif hyp == "delete":
            #    subprocess.check_call(["xdotool", "key", "Delete"])
            elif hyp == "document":
                subprocess.check_call(["xdotool", "key", "Ctrl+q"])
            elif hyp == "release":
                subprocess.check_call(["xdotool", "type", "~/releasespace/release-local"])
            elif hyp == "conjunction":
                subprocess.check_call(["xdotool", "type", "&"])
            elif hyp == "alternation":
                subprocess.check_call(["xdotool", "type", "|"])
            elif hyp == "above":
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "two above":
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "three above":
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "four above":
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "five above":
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "six above":
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
                subprocess.check_call(["xdotool", "key", "Up"])
            elif hyp == "down":
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "two down":
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "three down":
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "four down":
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "five down":
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "six down":
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
                subprocess.check_call(["xdotool", "key", "Down"])
            elif hyp == "supervisor":
                subprocess.check_call(["xdotool", "type", "/pqry/supervisor_logs/"])
            elif hyp == "format":
                subprocess.check_call(["xdotool", "key", "Ctrl+Alt+l"])
            elif hyp == "find":
                subprocess.check_call(["xdotool", "key", "Ctrl+f"])
            elif hyp == "erase":
                subprocess.check_call(["xdotool", "key", "Ctrl+BackSpace"])
            elif hyp == "escape":
                subprocess.check_call(["xdotool", "key", "Escape"])
            elif hyp == "lullaby":
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
                subprocess.check_call(["xdotool", "key", "Ctrl+Left"])
            elif hyp == "colon":
                subprocess.check_call(["xdotool", "type", ":"])
            elif hyp == "rename":
                subprocess.check_call(["xdotool", "key", "Ctrl+F6"])
            elif hyp == "equals":
                subprocess.check_call(["xdotool", "type", "="])
            elif hyp == "location":
                subprocess.check_call(["xdotool", "key", "Ctrl+l"])
            elif hyp == "search":
                subprocess.check_call(["xdotool", "key", "Ctrl+k"])
            elif hyp == "monkey":
                subprocess.check_call(["xdotool", "type", "@"])
            elif hyp == "confirm":
                subprocess.check_call(["xdotool", "type", "y"])
            elif hyp == "slash":
                subprocess.check_call(["xdotool", "type", "/"])

            print("{!s}".format(phrase))


if __name__ == "__main__":
    main()
