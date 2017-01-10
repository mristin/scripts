#!/usr/bin/env python


import subprocess
import multiprocessing
import re

import evdev


def main():
    """
    Main routine
    """
    name_re = re.compile(r'^N: Name="(?P<name>.*)"$')

    blocks=[]
    block=[]
    with open('/proc/bus/input/devices', 'rt') as fid:
        for line in fid.readlines():
            line = line.strip()
            if line == '':
                blocks.append(block)
                block=[]
            else:
                block.append(line)

    if len(block) > 0:
        blocks.append(block)

    mkeyboard_blocks=[]
    for block in blocks:
        for line in block:
            mtch = name_re.match(line)
            name = ''
            if mtch is not None:
                name = mtch.group("name")

            if name == 'MKEYBOARD':
                mkeyboard_blocks.append(block)

    eventids=[]
    for block in mkeyboard_blocks:
        for line in block:
            if line.startswith('H: Handlers='):
                pp = line[len('H: Handlers='):].split(' ')
                events = [p for p in pp if p.startswith('event')]
                if len(events) > 0:
                    eventid = events[0]
                    eventids.append(eventid)

    def display(eventid):
        pth='/dev/input/{}'.format(eventid)
        dev = evdev.InputDevice(pth)
        dev.grab()

        try:
            for evt in dev.read_loop():
                e = evdev.categorize(evt)
                if evt.type != evdev.ecodes.EV_KEY:
                    continue
                print("Path: %s, keystate: %s, keycode: %s" % (pth, e.keystate, e.keycode))

        except Exception as err:
            dev.ungrab()
            raise err

    procs=[]
    for eventid in eventids:
        proc=multiprocessing.Process(target=display, args=(eventid,))
        proc.start()
        procs.append(proc)

    print("Press a pedal.")

    for proc in procs:
        proc.join()

if __name__ == "__main__":
    main()
