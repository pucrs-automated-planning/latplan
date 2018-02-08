#!/bin/bash -x

set -e

ulimit -v 16000000000

./strips.py conv puzzle learn_plot_dump mandrill 3 3 49 20000

./strips.py conv puzzle learn_plot_dump mnist 3 3 49 20000

./strips.py conv puzzle learn_plot_dump spider 3 3 49 20000

./strips.py conv lightsout learn_plot_dump digital 4 49 20000

./strips.py conv lightsout learn_plot_dump twisted 4 49 20000

./strips.py conv hanoi learn_plot_dump 4 3 49 81

