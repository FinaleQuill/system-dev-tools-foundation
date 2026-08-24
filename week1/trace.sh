#!/usr/bin/env bash
set -x
name="trace-demo"
echo "hello $name"
test -f sample.txt || touch sample.txt
wc -c sample.txt
