#!/bin/bash
grep -rnw --include="*.go" -e "$1"
