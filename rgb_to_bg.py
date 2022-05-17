from imageio import imread, imwrite
import numpy as np
import glob
import shutil as sh
import os

name = "Task06_Lungs_RGB_2D_512_Balanced"

tr_root_folder = f"data/MSD/{name}/annotations/training"
val_root_folder = f"data/MSD/{name}/annotations/validation"

if not os.path.exists(tr_root_folder + "_copy"):
    sh.copytree(tr_root_folder, tr_root_folder + "_copy")
if not os.path.exists(val_root_folder + "_copy"):
    sh.copytree(val_root_folder, val_root_folder + "_copy")

for ind, image_path in enumerate(glob.glob(f"{tr_root_folder}/*.png")):
    image_rgb = imread(image_path)
    image_bg = image_rgb[:, :, 0]
    imwrite(image_path, image_bg)

for ind, image_path in enumerate(glob.glob(f"{val_root_folder}/*.png")):
    image_rgb = imread(image_path)
    image_bg = image_rgb[:, :, 0]
    imwrite(image_path, image_bg)
