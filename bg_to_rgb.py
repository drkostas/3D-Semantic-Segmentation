import numpy as np
from imageio import imread, imwrite
import glob
import os
import matplotlib.pyplot as plt

for ind, image_path in enumerate(glob.glob("data/MSD/Task09_Spleen_2D_512_Balanced/images/training/*.png")):
    image = imread(image_path)
    image_rgb = np.repeat(image[:, :, np.newaxis], 3, axis=2)
    image_path = image_path.replace("2D", "RGB_2D")
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    imwrite(image_path, image_rgb)


# imgplot = plt.imshow(image)
# print(image.shape)
# image2 = np.repeat(image[:, :, np.newaxis], 3, axis=2)
# print(image2.shape)
# imgplot = plt.imshow(image2)
# plt.show()
