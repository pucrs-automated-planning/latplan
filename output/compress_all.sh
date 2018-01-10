#!/bin/bash -x

for i in *; do tar cvzf $i.tar.bz2 $i; done