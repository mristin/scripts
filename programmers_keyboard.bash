#!/bin/bash
setxkbmap us
L=~/lock/underscore
if [ ! -f $L ]; then
  sudo xmodmap -e "keycode 20 = underscore minus underscore minus"
  touch $L
else 
  #and back to normal:
  sudo xmodmap -e "keycode 20 = minus underscore minus underscore"
  rm $L
fi

