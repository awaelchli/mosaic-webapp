from skimage import io
import numpy as np
from mosaic.src.Assignment1 import Assignment1
import mosaic.src.utils as utils
import os
from PIL import Image




""" This is where your main implementation of the Mosaicking algorithm goes.
    You should not train the model here, just use the saved model you trained beforehand. 
    Resize the uploaded image to a reasonable size to balance computation time and relative patch size.
"""


def mosaic(input_file, output_file):
    # array = io.imread(input_file)
    # io.imsave(output_file, array)
    # return True

    """
    Assignment 1a - Average Patch Features
    Assignment 1b - Nearest Neighbor Search

    """

    # Setting this to True will train the model (or pre-compute the features)
    # All models are automatically saved in the folder 'models'
    # After the model is trained well, you can set this to false
    train_features = False
    train_model = False


    # Load image and resize it to a fixed size (keeping aspect ratio)
    array = Image.open(input_file).convert('RGB')
    img = utils.resize_proportional(array, new_height=50)

    target_image = np.array(img) / 255

    # This will execute the Mosaicking algorithm of Assignment 1
    main = Assignment1()
    main.encode_features(train_features)
    print('ĥello')
    main.train(train_model)

    print(target_image.shape)

    output_image = main.mosaic(target_image)



    # Saving the image inside in project root folder
    output_image *= 255
    im = Image.fromarray(output_image.astype('uint8'))
    im.save(output_file)

    return True
