#!/bin/bash
grep -rn --include="*.py" -e "$1"
