from imageio import imread, imwrite
import numpy as np
import glob
import shutil as sh
import os

name = "Task06_Lungs_RGB_2D_512_Balanced"

tr_root_img_folder = f"data/MSD/{name}/images/training"
val_root_img_folder = f"data/MSD/{name}/images/validation"
tr_root_annot_folder = f"data/MSD/{name}/annotations/training"
val_root_annot_folder = f"data/MSD/{name}/annotations/validation"

for ind, image_path in enumerate(glob.glob(f"{tr_root_img_folder}/*.png")):
    image_bg = imread(image_path)
    if not isinstance(image_bg, np.ndarray):
        print("-----------------")
        print(image_path)
        print(type(image_bg))
    else:
        if image_bg.shape != (512, 512, 3):
            print("-----------------")
            print(image_path)
            print(type(image_bg))
for ind, image_path in enumerate(glob.glob(f"{val_root_img_folder}/*.png")):
    image_bg = imread(image_path)
    if not isinstance(image_bg, np.ndarray):
        print("-----------------")
        print(image_path)
        print(type(image_bg))
    else:
        if image_bg.shape != (512, 512, 3):
            print("-----------------")
            print(image_path)
            print(type(image_bg))

for ind, image_path in enumerate(glob.glob(f"{tr_root_annot_folder}/*.png")):
    image_bg = imread(image_path)
    if not isinstance(image_bg, np.ndarray):
        print("-----------------")
        print(image_path)
        print(type(image_bg))
    else:
        if image_bg.shape != (512, 512):
            print("-----------------")
            print(image_path)
            print(type(image_bg))
for ind, image_path in enumerate(glob.glob(f"{val_root_annot_folder}/*.png")):
    image_bg = imread(image_path)
    if not isinstance(image_bg, np.ndarray):
        print("-----------------")
        print(image_path)
        print(type(image_bg))
    else:
        if image_bg.shape != (512, 512):
            print("-----------------")
            print(image_path)
            print(type(image_bg))

