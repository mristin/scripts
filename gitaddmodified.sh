#!/bin/bash
for f in $(/usr/bin/git status|grep 'modified'|awk '{print $2}'); do
  /home/marko/scripts/gitadd.sh $f
done
