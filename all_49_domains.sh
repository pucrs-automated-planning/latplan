#!/bin/bash -x

#set -e

#trap exit SIGINT

./generate_domain.py domain samples/puzzle_mnist_3_3_49_20000_conv/all_actions.csv mnist domains_49/
./generate_domain.py domain samples/puzzle_spider_3_3_49_20000_conv/all_actions.csv spider domains_49/
./generate_domain.py domain samples/puzzle_mandrill_3_3_49_20000_conv/all_actions.csv mandrill domains_49/
./generate_domain.py domain samples/lightsout_digital_4_49_20000_conv/all_actions.csv lodigital domains_49/
./generate_domain.py domain samples/lightsout_twisted_4_49_20000_conv/all_actions.csv lotwisted domains_49/
./generate_domain.py domain samples/hanoi_4_3_49_81_conv/all_actions.csv hanoi domains_49/
