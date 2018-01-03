#!/bin/bash -x



./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_100 domains/mnist_actions.csv 100
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_10 domains/mnist_actions.csv 10