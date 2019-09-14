import os 
import pickle
import joblib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.neighbors import NearestNeighbors
import math
import random

from mosaic.src.base import Base
import mosaic.src.utils as utils
import random
import os

class Assignment1(Base):

    def __init__(self):
        super(Assignment1, self).__init__()
        self.data = pickle.load(open('./mosaic/src/features/cifar10/raw.pkl', 'rb'))
        self.features = None
        self.nn = self.get_model()
        self.model_file = './mosaic/src/models/nearest_neighbor.pkl'
        self.feature_file = './mosaic/src/features/cifar10/avg.pkl'

    def get_model(self):
        neighbor = NearestNeighbors(n_neighbors=1, metric=self.distance)
        return neighbor

    def get_patch(self, tile):
        tile_feature = self.feature(tile)
        _, inds = self.nn.kneighbors(tile_feature.reshape(1, -1))
        patch = self.data[inds[0]]
        return patch

    def get_patches(self, tiles):
        # N x (32 * 32 * 3)
        tile_features = self.feature(tiles)  # N x feat_size
        _, inds = self.nn.kneighbors(tile_features)
        patches = self.data[inds]
        return patches

    def encode_features(self, train=True):
        if train:
            self.features = np.stack([self.feature(patch) for patch in self.data])
            with open(self.feature_file, 'wb') as file:
                pickle.dump(self.features, file)
        else:
            with open(self.feature_file, 'rb') as file:
                self.features = pickle.load(file)

    def feature(self, x):

        reshaped_array = np.reshape(x, (32, 32, 3))
        # np.mean(reshaped_array, axis=(0, 1))
        a, b, c = np.mean(reshaped_array[:, :, 0]), np.mean(reshaped_array[:, :, 1]), np.mean(reshaped_array[:, :, 2])
        return np.array([a, b, c])
        

    

    def distance(self, x, y):
        array = np.array([y[0]- x[0], y[1] - x[1], y[2] - x[2]])
        return math.sqrt(array[0] ** 2 + array[1] ** 2 + array[2] ** 2)
        

    def train(self, train=True):
        if train:
            print('Fitting NN model ...')
            self.nn.fit(self.features.reshape(len(self.features), -1))
            # with open(self.model_file, 'wb') as f:
            joblib.dump(self.nn, self.model_file)

            print('... done.')
        elif os.path.exists(self.model_file):
            # with open(self.model_file, 'rb') as f:
            self.nn = joblib.load(self.model_file)
        else:
            print('Model not found.')

#
# if __name__ == '__main__':
#     os.makedirs('output/A1/mosaics/', exist_ok=True)
#     os.makedirs('models', exist_ok=True)
#     os.makedirs('features/cifar10', exist_ok=True)
#
#     """
#     Assignment 1a - Average Patch Features
#     Assignment 1b - Nearest Neighbor Search
#
#     """
#
#     # The program will start execution here
#     # Change the filename to load your favourite picture
#     file = './images/monkey.jpg'
#
#     # Setting this to True will train the model (or pre-compute the features)
#     # All models are automatically saved in the folder 'models'
#     # After the model is trained well, you can set this to false
#     train_features = True
#     train_model = True
#
#
#     # Load image and resize it to a fixed size (keeping aspect ratio)
#     img = Image.open(file).convert('RGB')
#     img = utils.resize_proportional(img, new_height=10000)
#     target_image = np.array(img) / 255
#
#     # This will execute the Mosaicking algorithm of Assignment 1
#     main = Assignment1()
#     main.encode_features(train_features)
#     main.train(train_model)
#
#     print(target_image.shape)
#
#     output_image = main.mosaic(target_image)
#
#     # Saving the image inside in project root folder
#     output_image *= 255
#     im = Image.fromarray(output_image.astype('uint8'))
#     im.save(utils.datetime_filename('output/A1/mosaics/mosaic.png'))
#
#     # Setup
#     main = Assignment1()
#     main.encode_features(False)
#     main.train(False)
#
#     os.makedirs('output/A1_test/features', exist_ok=True)
#     os.makedirs('output/A1_test/neighbors', exist_ok=True)
#
#     # test grid
#     patch_size = 10
#     original_width = 103
#     original_height = 121
#
#     nx, ny = utils.number_of_patches(original_width, original_height, patch_size)
#     new_width, new_height = utils.output_image_size(nx, ny, patch_size)
#     print(nx, ny)
#     print('new width is ' + str(new_width))
#     print('new height is ' + str(new_height))
#
#     # test feature
#     """
#     TO BE COMPLETED BY STUDENT
#
#     Change the code so that multiple columns are displayed.
#     Each column should contain a different (randomly picked) patch and it's mean color.
#     Run the script first to see what the output is.
#
#     """
#     num_cols = 3  # CHANGE THIS
#
#     i = 0
#     for col in range(num_cols):
#         i += 1
#         rdm_number = random.randrange(50000)
#         patch_idx = rdm_number
#         patch = main.data[patch_idx]
#         feature = main.feature(patch)
#         patch_mean = feature.reshape(1, 1, 3).repeat(32, 0).repeat(32, 1)
#
#         # grid plot of size 2 x num_cols
#         plt.subplot(2, num_cols, i)
#         plt.title(str(patch_idx))
#         plt.imshow(patch)
#
#         plt.subplot(2, num_cols, num_cols + i)
#         plt.imshow(patch_mean)
#
#     fig = plt.gcf()
#     plt.show()
#     fname = utils.datetime_filename('output/A1_test/features/grid.png')
#     fig.savefig(fname, format='png', dpi=300)
#
#     # test distance
#     patch1 = main.data[0]
#     patch2 = main.data[1]
#     dist = main.distance(main.feature(patch1), main.feature(patch1))
#     print('Distance between same patches: {:.4f}'.format(dist))
#
#     dist = main.distance(main.feature(patch1), main.feature(patch2))
#     print('Distance between two different patches: {:.4f}'.format(dist))
#
#     # test neighbours
#     num_cols = 3
#     num_rows = 3
#
#     main.nn.n_neighbors = num_cols
#     i = 0
#
#     for row in range(num_rows):
#         patch_idx = np.random.randint(0, len(main.data))
#         patch = main.data[patch_idx]
#         neighbors = main.get_patch(patch).reshape(-1, 32, 32, 3)
#
#         for col in range(num_cols):
#             i += 1
#
#             if col == 0:
#                 plt.subplot(num_rows, num_cols, i)
#                 plt.title(str(patch_idx))
#                 plt.imshow(patch)
#             else:
#                 plt.subplot(num_rows, num_cols, i)
#                 # plt.title(str(patch_idx))
#                 plt.imshow(neighbors[col])
#
#     fig = plt.gcf()
#     plt.show()
#     fname = utils.datetime_filename('output/A1_test/neighbors/grid.png')
#     fig.savefig(fname, format='png', dpi=300)