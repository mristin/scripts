#!/usr/bin/env bash
cwid=$(xdotool getwindowfocus) # Save the current window
echo cwid: $cwid
pid=$(ps -lA|grep firefox|~/workspace/scripts/col.bash 4|tail -1)
echo pid: $pid
twid=$(xdotool search --pid $pid|tail -1)
echo twid: $twid
xdotool windowactivate $twid
sleep 0.1 # The key event might be sent before the window has been fully activated
xdotool key --window $twid F5
xdotool windowactivate $cwid # Done, now go back to where we were
