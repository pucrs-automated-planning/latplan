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


class EncoderDecoder():
    """
        Encoder/Decoder class to turn images into a latent representations and
        reconstruct images from latent representations.
    """
    def __init__(self, network_folder):
        
        self.network_folder = network_folder
        self.sae = default_networks[get_ae_type(self.network_folder)](self.network_folder).load(allow_failure=True)

    @staticmethod
    def _open_image(image_path):
        # Open and normalize an image by its path.
        img = normalize(misc.imread(image_path))
        return img

    @staticmethod
    def _save_img(image, output_path):

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

        image_name = os.path.basename(image_path)
        path_to_img = os.path.dirname(image_path)
        return  os.path.join(path_to_img, mode + '_' + image_name)

    def encode(self, image_path, save=False):

        image_path = os.path.realpath(image_path)

        image = self._open_image(image_path)
        encode = self.sae.encode_binary(np.expand_dims(image,0))[0].round().astype(int)    

        if save:
            output_path = self._get_output_path(image_path, 'encode')
            self._save_img(encode, output_path)

        return encode

    def decode(self, image_path, save=False):

        image_path = os.path.realpath(image_path)

        image = self._open_image(image_path)
        decode = self.sae.decode_binary(np.array([image]))

        if save:
            output_path = self._get_output_path(image_path, 'decode')
            self._save_img(decode, output_path)

        return decode

    def convert_folder(self, folder_path, mode='encode'):

        # Get file in folder.
        images = os.listdir(folder_path)

        for image in images:

            image_path = os.path.join(folder_path, image)

            try:
                image = self._open_image(image_path)
            except:
                print("Problem when opening 'image': %s" % image_path)
                continue

            if mode == 'encode':
                self.encode(image_path, save=True)
            else:
                self.decode(image_path, save=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('network_foder', metavar='net_foder', 
                        help='Path containing a trained network for a specific domain.')
    args = parser.parse_args()

    enc_dec = EncoderDecoder(args.network_foder)

    image_path = "/usr/share/datasets/8_puzzle_mnist/test_folder/012345678.jpg"

    dec = enc_dec.encode(image_path, save=True)
    print(dec)
    # enc = enc_dec.decode()    

    # network_dir = "samples/puzzle_mnist_3_3_36_20000_conv/"
    

    