#!/usr/bin/env bash

var=$(mktemp /tmp/XXXXXXXX.png)
scrot -zm $var
exit_code=$?
if [[ $exit_code -ne 0 ]]; then
  echo False
  exit $exit_code
fi
echo $var
