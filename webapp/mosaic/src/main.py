from skimage import io
import numpy as np


""" This is where your main implementation of the Mosaicking algorithm goes.
    You should not train the model here, just use the saved model you trained beforehand. 
    Resize the uploaded image to a reasonable size to balance computation time and relative patch size.
"""


def mosaic(input_file, output_file):
    array = io.imread(input_file)
    io.imsave(output_file, array)
    return True
