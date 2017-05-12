#!/bin/bash

FILES=$(gitdifftomaster.sh |grep '^[MA]'|awk '{print $2}')
BACKUP=$HOME/co

echo "$FILES"
for f in `echo $FILES`; do
	base=~/co/`date +%Y-%m-%dT%H-%M-%S`; 
	mkdir -p $base; 
	d=$base/`dirname $f`; 
	mkdir -p $d; 
	cp -v $f $d/; 
done
	

