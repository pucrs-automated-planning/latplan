import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
import os
import random
import copy
import keras

from keras.layers import Input, Dense, Lambda, Dropout, BatchNormalization, GaussianNoise
from keras.models import Model, Sequential
from keras import backend as K
from keras import objectives
from keras.datasets import mnist
from keras.activations import softmax
from keras.objectives import binary_crossentropy as bce
from keras.objectives import mse
from scipy import misc
from sklearn.preprocessing import Binarizer

#img = misc.imread('/usr/share/datasets/KSCGR/hof/data1/boild-egg/hof256/0.jpg')
batch_size = 1000
latent_dim = 1764
M = 2
_N = 7
N = _N*_N

tau = K.variable(5.0, name="temperature")

def sampling(logits_y):
    U = K.random_uniform(K.shape(logits_y), 0, 1)
    y = logits_y - K.log(-K.log(U + 1e-20) + 1e-20) # logits + gumbel noise
    y = softmax(K.reshape(y, (-1, N, M)) / tau)
    y = K.reshape(y, (-1, N*M))
    return y


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


x = Input(shape=(latent_dim,))

_encoder = Sequential([
        GaussianNoise(0.1, input_shape=(latent_dim,)),
        Dense(4000, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(4000, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(M*N),
    ])


logits_y = _encoder(x)
z = Lambda(sampling, output_shape=(M*N,))(logits_y)
encoder = Model(x,z)

decoder = Sequential([
        Dropout(0.4, input_shape=(N*M, )),
        Dense(4000, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(4000, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(latent_dim, activation='sigmoid')
    ])

x_hat = decoder(z)

def gumbel_loss(x, x_hat):
    q_y = K.reshape(logits_y, (-1, N, M))
    q_y = softmax(q_y)
    log_q_y = K.log(q_y + 1e-20)
    kl_tmp = q_y * (log_q_y - K.log(1.0/M))
    KL = K.sum(kl_tmp, axis=(1, 2))
    elbo = latent_dim * bce(x, x_hat) - KL
    # elbo = latent_dim * mse(x, x_hat) - KL 
    return elbo

vae = Model(x, x_hat)
vae.compile(optimizer='adam', loss=gumbel_loss)
#encoder = Model()
encoder.load_weights('model_new/encoder.h5')
decoder.load_weights('model_new/decoder.h5')
test = []
test.append(misc.imread("../eight-puzzle_mnist/102345678.jpg"))
test.append(misc.imread("../eight-puzzle_mnist/781023456.jpg"))
test = np.array(test)
test = test.astype('float32') / 255.
b = Binarizer(0.3)
for img in test:
	b.transform(img, copy=False)
test = test.reshape((len(test), np.prod(test.shape[1:])))
code = encoder.predict(test)
code = code.astype(int)
code2 = decoder.predict(code)

print len(code[0])
plt.figure(figsize=(30, 5))
plt.imshow(code2[1].reshape(42, 42), cmap='gray')
plt.show()
