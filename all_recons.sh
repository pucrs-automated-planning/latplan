#!/bin/bash -x


#MNIST

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_10 domains/mnist_actions.csv 10

#SPIDER

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_10 domains/spider_actions.csv 10

#MANDRILL

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_10 domains/mandrill_actions.csv 10

#HANOI

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb01 output/pb01_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb01 output/pb01_hanoi_out_70 domains/hanoi_actions.csv 70
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb01 output/pb01_hanoi_out_50 domains/hanoi_actions.csv 50
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb01 output/pb01_hanoi_out_30 domains/hanoi_actions.csv 30
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb01 output/pb01_hanoi_out_10 domains/hanoi_actions.csv 10

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb02 output/pb02_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb02 output/pb02_hanoi_out_70 domains/hanoi_actions.csv 70 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb02 output/pb02_hanoi_out_50 domains/hanoi_actions.csv 50 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb02 output/pb02_hanoi_out_30 domains/hanoi_actions.csv 30 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb02 output/pb02_hanoi_out_10 domains/hanoi_actions.csv 10 True

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb03 output/pb03_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb03 output/pb03_hanoi_out_70 domains/hanoi_actions.csv 70
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb03 output/pb03_hanoi_out_50 domains/hanoi_actions.csv 50
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb03 output/pb03_hanoi_out_30 domains/hanoi_actions.csv 30
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb03 output/pb03_hanoi_out_10 domains/hanoi_actions.csv 10

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb04 output/pb04_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb04 output/pb04_hanoi_out_70 domains/hanoi_actions.csv 70
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb04 output/pb04_hanoi_out_50 domains/hanoi_actions.csv 50
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb04 output/pb04_hanoi_out_30 domains/hanoi_actions.csv 30
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb04 output/pb04_hanoi_out_10 domains/hanoi_actions.csv 10

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb05 output/pb05_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb05 output/pb05_hanoi_out_70 domains/hanoi_actions.csv 70
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb05 output/pb05_hanoi_out_50 domains/hanoi_actions.csv 50
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb05 output/pb05_hanoi_out_30 domains/hanoi_actions.csv 30
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb05 output/pb05_hanoi_out_10 domains/hanoi_actions.csv 10

./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb06 output/pb06_hanoi_out_100 domains/hanoi_actions.csv 100 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb06 output/pb06_hanoi_out_70 domains/hanoi_actions.csv 70 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb06 output/pb06_hanoi_out_50 domains/hanoi_actions.csv 50 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb06 output/pb06_hanoi_out_30 domains/hanoi_actions.csv 30 True
./generate_domain.py recon samples/hanoi_4_3_36_81_conv/ domains/hanoi_domain.pddl problems/hanoi/pb06 output/pb06_hanoi_out_10 domains/hanoi_actions.csv 10 True