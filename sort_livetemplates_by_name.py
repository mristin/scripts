#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET


def indent(elem, level=0, more_sibs=False):
    i = "\n"
    if level:
        i += (level - 1) * '  '
    num_kids = len(elem)
    if num_kids:
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
            if level:
                elem.text += '  '
        count = 0
        for kid in elem:
            indent(kid, level + 1, count < num_kids - 1)
            count += 1
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
            if more_sibs:
                elem.tail += '  '
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            if more_sibs:
                elem.tail += '  '


def main() -> None:
    """"
    Main routine
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path to the livetemplate .xml file", required=True)
    parser.add_argument("-o", "--output", help="path where the output will be stored; if omitted, prints to stdout")
    args = parser.parse_args()

    pth = args.input
    assert isinstance(pth, str)

    tree = ET.parse(pth)
    root = tree.getroot()

    new_root = ET.Element(root.tag, root.attrib)
    lst = []
    for child in root:
        lst.append(child)

    lst.sort(key=lambda child: child.get("name"))

    for child in lst:
        new_root.append(child)

    indent(new_root)

    out = ET.tostring(new_root).decode()

    if args.output is None:
        sys.stdout.write(out)
    else:
        with open(args.output, 'wt') as fid:
            fid.write(out)


if __name__ == "__main__":
    main()
