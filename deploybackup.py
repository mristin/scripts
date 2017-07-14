#!/bin/bash

bld.sh
rm -rf ~/temp/deleteme
src/py/devop/gce/backup/deployry.py -r ~/releasespace/release-local -p ~/temp/deleteme --overwrite
