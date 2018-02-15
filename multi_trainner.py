#!/usr/bin/env python3

from action import *
from subprocess import call
from os import listdir
from os.path import isfile, join
import os, errno
import ast
import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from encode_decode import EncoderDecoder
from latplan.util.plot import *
import numpy as np
import generate_domain as gd
import strips as st 


#Latent layer size
N = 36
FD_PATH = '../fast_downward/'
MP_PATH = '../MauPlanner/'
SIZE_H = 42
SIZE_W = 42
DATASETS = { 
'mandrill': [3, 3, 20000],
'mnist': [3, 3, 20000],
'spider': [3, 3, 20000],
'digital': [4,20000],
'twisted': [4,20000],
'hanoi': [4,3,81]
}


def manager():
    latent_size = 25
    st.set_globals('conv', 'learn_plot_dump')
    st.puzzle(type='mnist',width=DATASETS['mnist'][0],height=DATASETS['mnist'][1],N=latent_size,num_examples=DATASETS['mnist'][2])
    st.puzzle(type='mandrill',width=DATASETS['mandrill'][0],height=DATASETS['mandrill'][1],N=latent_size,num_examples=DATASETS['mandrill'][2])
    st.puzzle(type='spider',width=DATASETS['spider'][0],height=DATASETS['spider'][1],N=latent_size,num_examples=DATASETS['spider'][2])
    st.lightsout(type='digital',size=DATASETS['digital'][0],N=latent_size,num_examples=DATASETS['digital'][-1])
    st.lightsout(type='twisted',size=DATASETS['twisted'][0],N=latent_size,num_examples=DATASETS['twisted'][-1])
    st.lightsout(disks=DATASETS['hanoi'][0],towers=DATASETS['hanoi'][1],N=latent_size,num_examples=DATASETS['hanoi'][2])
#if __name__ == '__main__':
#    import sys
#    if sys.argv[1] == 'domain':
#        module_create_domain(*sys.argv[2:])
#    elif sys.argv[1] == 'recon':
#        set_up_pgr(*sys.argv[2:])       
    #if len(sys.argv) < 3:
     #   sys.exit("{} [networkdir] [problemdir]".format(sys.argv[0]))
    #main(*sys.argv[1:])
#    sys.exit()
#set_up_pgr('samples/puzzle_mnist_3_3_36_20000_conv/','mnist01/domain.pddl', 'pb01', 'pb01_out')
