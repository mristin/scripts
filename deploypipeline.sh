#!/bin/bash
rm -rf ~/temp/deleteme
src/py/devop/gce/pipeline/deployry.py --config_name $1 --release_dir ~/releasespace/release-local --overwrite --package_dir ~/temp/deleteme
