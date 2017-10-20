#!/usr/bin/env python2

"""
Maps the pedals to the key events.

To find out which device corresponds to which /dev/input/eventX path, use:
cat /proc/bus/input/devices

The configuration of the initial keys needs to be set in:
cat /etc/udev/hwdb.d/foot-pedal.hwdb
keyboard:usb:v0426p3011*
 KEYBOARD_KEY_0x7001e=esc
 KEYBOARD_KEY_0x7001f=leftalt
 KEYBOARD_KEY_0x70020=leftctrl

For the list of xdotool key identifiers, see:
http://www.linux.org/threads/xdotool-keyboard.6414/
"""

import subprocess
import multiprocessing

import evdev

backpedal_pth = "/dev/input/event5"
frontpedal_pth = "/dev/input/event7"
leftpedal_pth = ""
rightpedal_pth = ""
kickleft_pth = "/dev/input/event4"
kickright_pth = "/dev/input/event6"

def current_active_program():
    pid=int(subprocess.check_output(["xdotool", "getactivewindow", "getwindowpid"]).strip())
    path=subprocess.check_output(['readlink', '-f', '/proc/{}/exe'.format(pid)]).strip()
    return path

def do_leftpedal():
    if leftpedal_pth == '':
        return

    dev = evdev.InputDevice(leftpedal_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            if e.keystate == e.key_down:
                if e.keycode == "KEY_LEFTALT":
                    subprocess.call(["xdotool", "keydown", "End"])

                elif e.keycode == "KEY_ESC":
                    subprocess.call(["xdotool", "keydown", "Home"])

                else:
                    raise RuntimeError("Unhandled keycode: %s" % e.keycode)

            elif e.keystate == e.key_up:
                if e.keycode == "KEY_LEFTALT":
                    subprocess.call(["xdotool", "keyup", "End"])

                elif e.keycode == "KEY_ESC":
                    subprocess.call(["xdotool", "keyup", "Home"])

                else:
                    raise RuntimeError("Unhandled keycode: %s" % e.keycode)

    except e:
        dev.ungrab()
        raise e


def do_rightpedal():
    if rightpedal_pth == '':
        return

    dev = evdev.InputDevice(rightpedal_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            if e.keystate == e.key_down:
                if e.keycode == "KEY_LEFTALT":
                    subprocess.call(["xdotool", "keydown", "ctrl+Right"])

                elif e.keycode == "KEY_ESC":
                    subprocess.call(["xdotool", "keydown", "ctrl+Left"])

                else:
                    raise RuntimeError("Unhandled keycode: %s" % e.keycode)

            elif e.keystate == e.key_up:
                if e.keycode == "KEY_LEFTALT":
                    subprocess.call(["xdotool", "keyup", "ctrl+Right"])

                elif e.keycode == "KEY_ESC":
                    subprocess.call(["xdotool", "keyup", "ctrl+Left"])

                else:
                    raise RuntimeError("Unhandled keycode: %s" % e.keycode)

    except e:
        dev.ungrab()
        raise e


def do_frontpedal():
    if frontpedal_pth == '':
        return

    dev = evdev.InputDevice(frontpedal_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            title = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"])
            if e.keystate == e.key_down:
                if e.keycode == "KEY_3":
                    subprocess.call(["xdotool", "keydown", "ctrl"])

                elif e.keycode == "KEY_2":
                    subprocess.call(["xdotool", "keydown", "alt"])


            elif e.keystate == e.key_up:
                if e.keycode == "KEY_3":
                    subprocess.call(["xdotool", "keyup", "ctrl"])

                elif e.keycode == "KEY_2":
                    subprocess.call(["xdotool", "keyup", "alt"])


                elif e.keycode == "KEY_1":
                    subprocess.call(["xdotool", "key", "Tab"])


                else:
                    print "Unhandled keycode: %s" % e.keycode

    except e:
        dev.ungrab()
        raise e


def do_backpedal():
    if backpedal_pth == '':
        return

    dev = evdev.InputDevice(backpedal_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            if e.keystate == e.key_up:
                title = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"])
                program = current_active_program()

                if e.keycode == "KEY_1":
                    if "Firefox" in title:
                        subprocess.call(["xdotool", "key", "ctrl+Page_Up"])
                    elif "PyCharm" in title:
                        subprocess.call(["xdotool", "key", "alt+Left"])
                    elif "Gogland" in title:
                        subprocess.call(["xdotool", "key", "alt+Left"])
                    elif "CLion" in title:
                        subprocess.call(["xdotool", "key", "alt+Left"])
                    elif "gnome-terminal" in program:
                        subprocess.call(["xdotool", "key", "ctrl+Page_Up"])

                elif e.keycode == "KEY_2":
                    if "Firefox" in title:
                        subprocess.call(["xdotool", "key", "ctrl+Page_Down"])
                    elif "PyCharm" in title:
                        subprocess.call(["xdotool", "key", "alt+Right"])
                    elif "Gogland" in title:
                        subprocess.call(["xdotool", "key", "alt+Right"])
                    elif "CLion" in title:
                        subprocess.call(["xdotool", "key", "alt+Right"])
                    elif "gnome-terminal" in program:
                        subprocess.call(["xdotool", "key", "ctrl+Page_Down"])

    except e:
        dev.ungrab()
        raise e

def do_kickright():
    if kickright_pth=='':
        return

    dev = evdev.InputDevice(kickright_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            if e.keystate == e.key_up:
                if e.keycode == "KEY_1":
                    #subprocess.call(["xdotool", "keyup", "Down"])
                    subprocess.call(["xdotool", "type", "Hi Andrea,"])
            #elif e.keystate == e.key_down:
            #    if e.keycode == "KEY_1":
            #        subprocess.call(["xdotool", "keydown", "Down"])

    except e:
        dev.ungrab()
        raise e

def do_kickleft():
    if kickleft_pth=='':
        return

    dev = evdev.InputDevice(kickleft_pth)
    dev.grab()

    try:
        for evt in dev.read_loop():
            e = evdev.categorize(evt)
            if evt.type != evdev.ecodes.EV_KEY:
                continue

            if e.keystate == e.key_up:
                if e.keycode == "KEY_1":
                    subprocess.call(["xdotool", "keyup", "ctrl+shift+n"])
            elif e.keystate == e.key_down:
                if e.keycode == "KEY_1":
                    subprocess.call(["xdotool", "keydown", "ctrl+shift+n"])

            #if e.keystate == e.key_up:
            #    if e.keycode == "KEY_1":
            #        subprocess.call(["xdotool", "keyup", "Up"])
            #elif e.keystate == e.key_down:
            #    if e.keycode == "KEY_1":
            #        subprocess.call(["xdotool", "keydown", "Up"])

    except e:
        dev.ungrab()
        raise e


def main():
    pp = []

    for func in [do_backpedal, do_frontpedal, do_leftpedal, do_rightpedal, do_kickleft, do_kickright]:
        p = multiprocessing.Process(target=func)
        p.start()
        pp.append(p)

    for p in pp:
        p.join()


if __name__ == "__main__":
    main()
