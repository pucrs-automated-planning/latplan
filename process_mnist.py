import os
import sys
import cv2
import keras
import random
import numpy as np
from keras.datasets import mnist
from itertools import permutations

# CONSTANTS.
n_width, n_height = 28, 28  # Numbers size.
p_width, p_height = 42, 42  # Puzzle size.
n_elem = 9  # Number of numbers for the 8-puzzle.

def select_numbers(numbers):
    # Select 9 images to make 8-puzzle.
    for i in numbers:
        numbers[i] = random.choice(digits[i])


def save_image(image_name, image):

    if not os.path.exists('test_images'):
        os.makedirs('test_images')

    image_output = os.path.join('test_images', image_name)

    cv2.imwrite(image_output, image)


if __name__ == "__main__":

    numbers = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None
    }

    # Get MNIST.
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Divide images according to their class.
    digits = dict()

    for i in xrange(x_train.shape[0]):

        if y_train[i] not in digits:
            digits[y_train[i]] = [x_train[i]]
        else:
            digits[y_train[i]].append(x_train[i])

    select_numbers(numbers)

    iter_perm = permutations(numbers.keys(), n_elem)  # Perform permutation over the 9 possibilities.

    for num_pos in iter_perm:
        # Run over different number positions.
        
        num_pos = np.array(list(num_pos)).reshape(3, 3)  # Reshape to turn it into a matrix.
        
        new_image = np.zeros(shape=(p_width, p_height))  # Create a new image to receive the 8-puzze.

        for i in range(num_pos.shape[0]):            
            for j in range(num_pos.shape[1]):
                # Get the position of each number in the new image.

                number = num_pos[i][j]  # Get the number corresponding to the position.

                img = numbers[number]
                res = cv2.resize(img,(n_width/2, n_height/2), interpolation = cv2.INTER_CUBIC)  # Resize image.

                running_line, running_column = i * res.shape[0], j * res.shape[1]  # Define the initial positions for line and column in the new image.
                max_line, max_column = res.shape[0] + (i * res.shape[0]), res.shape[1] + (j * res.shape[1])  # Define the max values in the new
                                                                                                             # image to the selected number.
                new_image[running_line:max_line, running_column:max_column] = res
                
                # for ii in range(res.shape[0]):

                #     if running_line == max_line:
                #         # Restart the line when it reaches the maximum value.
                #         running_line = i * res.shape[0]

                #     for jj in range(res.shape[1]):
                #         new_image[running_line][running_column] = res[ii][jj]
                #         running_column += 1
                        
                #         if running_column == max_column:
                #             # Restart the column when it reaches the maximum value.
                #             running_column = j * res.shape[1]
                    
                #     running_line += 1
        
        # Create the image name.
        image_name = ''.join([str(x) for x in list(num_pos.reshape(3*3))]) + '.jpg'

        # Save image.
        save_image(image_name, new_image)