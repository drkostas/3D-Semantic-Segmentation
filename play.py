from imageio import imread, imwrite
import numpy as np
import glob
import shutil as sh
import os
from matplotlib import pyplot as plt

name = "Task06_Lungs_RGB_2D_512_Balanced"

tr_root_img_folder = f"data/MSD/{name}/images/training"
val_root_img_folder = f"data/MSD/{name}/images/validation"
tr_root_annot_folder = f"data/MSD/{name}/annotations/training"
val_root_annot_folder = f"data/MSD/{name}/annotations/validation"

image_bg = imread(tr_root_img_folder + "/lung_018_Slice_147.png")
plt.imshow(image_bg)
plt.show()
