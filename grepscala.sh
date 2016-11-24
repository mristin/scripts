#!/bin/bash
grep -rnw --include="*.scala" -e "$1"
