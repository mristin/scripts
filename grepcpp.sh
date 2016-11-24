#!/bin/bash
grep -rnw --include="*.cpp" --include="*.h" --include="*.hpp" -e "$1"
