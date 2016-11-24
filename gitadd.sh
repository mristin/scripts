#!/bin/bash
for PATH in "$@"; do
  if [[ $PATH =~ \.go$ ]]; then
    /home/mristin/apps/goLibs1.5.2/bin/goimports -w $PATH
  fi
  /usr/bin/git add $1
done
