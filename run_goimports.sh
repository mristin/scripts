#!/bin/bash
PATH="$1"
if [ "$PATH" == "*.go" ]; then
  goimports -w $PATH
fi
