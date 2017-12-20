import os
import cv2
import math
import latplan
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from latplan.util import get_ae_type
from latplan.model import default_networks
from latplan.puzzles.util import preprocess, normalize
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)

GPU_NUMBER = '1'

class EncoderDecoder():
    """
        Encoder/Decoder class to turn images into latent representations and
        reconstruct images from latent representations.
    """
    def __init__(self, network_folder):
        # Initialize autoencoder using the network_folder.
        self.network_folder = network_folder
        self.sae = default_networks[get_ae_type(self.network_folder)](self.network_folder).load(allow_failure=True)

    @staticmethod
    def _open_image(image_path):
        # Open and normalize an image by its path.
        img = normalize(misc.imread(image_path))
        return img

    @staticmethod
    def _save_img(image, output_path):
        # Save an image to the destination path.
        # TODO: Make it work, please.
        w = 4
        l = 4
        h = int(math.ceil(l/w))
        plt.figure(figsize=(w*1.5, h*1.5))
        i = 0
        ax = plt.subplot(h,w,i+1)
        try:
            plt.imshow(image,interpolation='nearest',cmap='gray',)
        except TypeError:
            TypeError("Invalid dimensions for image data: image={}".format(np.array(image).shape))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        print(image_path) if verbose else None
        plt.tight_layout()
        plt.savefig(image_path)
        plt.close()

    @staticmethod
    def _get_output_path(image_path, mode):
        # From a given path, create an output_path with the correct mode (encode, decode).
        image_name = os.path.basename(image_path)
        path_to_img = os.path.dirname(image_path)
        return  os.path.join(path_to_img, mode + '_' + image_name)

    def encode(self, image_path, open_img=False):
        # Turn an image to a latent representation.
        # Set open_img True if the image_path is a path to an image and needs to be opened.
        if open_img:
            image_path = os.path.realpath(image_path)
            image = self._open_image(image_path)

        return self.sae.encode_binary(np.expand_dims(image,0))[0].round().astype(int)    

    def decode(self, encoded_img, open_img=False):
        # Turn a latent representation to an image.
        # Set open_img True if the image_path is a path to an image and needs to be opened.
        if open_img:
            encoded_img = os.path.realpath(encoded_img)
            encoded_img = self._open_image(encoded_img)

        return self.sae.decode_binary(np.array([encoded_img]))


if __name__ == '__main__':

    os.environ['CUDA_VISIBLE_DEVICES'] = GPU_NUMBER
    
    parser = argparse.ArgumentParser()

    parser.add_argument('network_foder', metavar='net_foder', 
                        help='Path containing a trained network for a specific domain.')
    args = parser.parse_args()

    enc_dec = EncoderDecoder(args.network_foder)

    image_path = "/usr/share/datasets/8_puzzle_mnist/test_folder/012345678.jpg"

    dec = enc_dec.encode(image_path, open_img=True)
    print(dec)
    
    # network_dir = "samples/puzzle_mnist_3_3_36_20000_conv/"
    

    