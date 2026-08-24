#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file>" >&2
  exit 2
fi
if [ -f "$1" ]; then
  echo "File exists: $1"
else
  echo "File not found: $1"
  exit 1
fi
