#!/bin/bash -x

#set -e

#trap exit SIGINT

./generate_domain.py domain samples/puzzle_mnist_3_3_36_20000_conv/all_actions.csv mnist domains/
./generate_domain.py domain samples/puzzle_spider_3_3_36_20000_conv/all_actions.csv spider domains/
./generate_domain.py domain samples/puzzle_mandrill_3_3_36_20000_conv/all_actions.csv mandrill domains/
./generate_domain.py domain samples/lightsout_digital_4_36_20000_conv/all_actions.csv lodigital domains/
./generate_domain.py domain samples/lightsout_twisted_4_36_20000_conv/all_actions.csv lotwisted domains/
./generate_domain.py domain samples/hanoi_4_3_36_81_conv/all_actions.csv hanoi domains/
