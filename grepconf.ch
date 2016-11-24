#!/bin/bash
grep -rnw --include="*.conf" -e "$1"
