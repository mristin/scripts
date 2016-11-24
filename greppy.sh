#!/bin/bash
grep -rnw --include="*.py" -e "$1"
