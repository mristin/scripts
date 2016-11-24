#!/bin/bash
grep -rnw --include="*.sbt" -e "$1"
