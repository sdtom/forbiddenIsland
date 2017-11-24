#!/bin/bash
pushd ./logs
cat "`ls -t | head -1`" | more
popd
