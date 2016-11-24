#!/bin/bash
awk '{print $'$(echo $* | sed -e 's/ /,$/g')'}'
