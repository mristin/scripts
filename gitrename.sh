#!/bin/bash
if [ "$#" -eq 0 ]; then
  BRANCH=`~/scripts/git-current-branch.py .`
elif [ "$#" -eq 1 ]; then 
  BRANCH=$1
else
  echo "Usage: `basename $0` {branch}"
fi
