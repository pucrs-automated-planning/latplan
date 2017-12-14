#!/usr/bin/env python3
import warnings
import config
import numpy as np
import latplan
from latplan.model import default_networks, ActionAE, Discriminator, PUDiscriminator
from latplan.util import get_ae_type, bce, mae, mse, ensure_directory
from latplan.util.plot import plot_grid
import os.path
import keras.backend as K
import tensorflow as tf
import math

float_formatter = lambda x: "%.3f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})

sae = None
oae = None
ad  = None
sd  = None
ad2  = None
sd2  = None
sd3 = None
cae = None
combined_discriminator = None

available_actions = None
inflation = 5

image_threshold = 0.1
image_diff = mae

OPEN   = 0
CLOSED = 1

def main(network_dir, problem_dir):
    global sae, oae, ad, ad2, sd, sd2, sd3, cae, combined_discriminator, available_actions
    
    p = latplan.util.puzzle_module(network_dir)

    sae = default_networks[get_ae_type(network_dir)](network_dir).load(allow_failure=True)
    try:
        ad  = PUDiscriminator(sae.local("_ad/")).load(allow_failure=True)
    except:
        ad  = Discriminator(sae.local("_ad/")).load(allow_failure=True)
    # sd  = Discriminator(sae.local("_sd/")).load(allow_failure=True)
    # ad2 = Discriminator(sae.local("_ad2/")).load(allow_failure=True)
    # sd2 = Discriminator(sae.local("_sd2/")).load(allow_failure=True)
    sd3 = PUDiscriminator(sae.local("_sd3/")).load()
    discriminator = default_networks['CombinedDiscriminator2'](sae,sd3)

    def problem(path):
        return os.path.join(problem_dir,path)
    def network(path):
        root, ext = os.path.splitext(path)
        return "{}_{}{}".format(ensure_directory(network_dir).split("/")[-2], root, ext)
    def search(path):
        root, ext = os.path.splitext(path)
        return "{}_{}{}".format(searcher, root, ext)


    from scipy import misc
    from latplan.puzzles.util import preprocess, normalize
    # is already enhanced, equalized
    init_image = normalize(misc.imread(problem("init.png")))
    goal_image = normalize(misc.imread(problem("goal.png")))
    print("init:",init_image.min(),init_image.max(),)
    print("goal:",goal_image.min(),goal_image.max(),)
    init = sae.encode_binary(np.expand_dims(init_image,0))[0].round().astype(int)
    goal = sae.encode_binary(np.expand_dims(goal_image,0))[0].round().astype(int)
    print(init)
    print(goal)
    rec = sae.decode_binary(np.array([init,goal]))
    init_rec, goal_rec = rec
    print("init (reconstruction):",init_rec.min(),init_rec.max(),)
    print("goal (reconstruction):",goal_rec.min(),goal_rec.max(),)

    print("init BCE:",bce(init_image,init_rec))
    print("init MAE:",mae(init_image,init_rec))
    print("init MSE:",mse(init_image,init_rec))
  

    print("goal BCE:",bce(goal_image,goal_rec))
    print("goal MAE:",mae(goal_image,goal_rec))
    print("goal MSE:",mse(goal_image,goal_rec))


#if __name__ == '__main__':
#    import sys
#    if len(sys.argv) < 3:
#        sys.exit("{} [networkdir] [problemdir]".format(sys.argv[0]))
#    main(*sys.argv[1:])


def test():
    # ./trivial-planner.py samples/puzzle_mnist33_fc/ trivial-planner-instances/latplan.puzzles.puzzle_mnist/0-0/
    main("samples/puzzle_mnist_3_3_36_20000_conv/",
         "problem-instances/vanilla/latplan.puzzles.puzzle_mnist/007-000-000")

test()    
