#!/bin/bash -x

for i in *; do tar jcvf $i.tar.bz2 $i/*; done
