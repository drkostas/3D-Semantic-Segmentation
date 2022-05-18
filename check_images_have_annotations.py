import glob
import os

name = "Task09_Spleen_RGB_2D_512"

tr_root_img_folder = f"data/MSD/{name}/images/training"
val_root_img_folder = f"data/MSD/{name}/images/validation"
tr_root_annot_folder = f"data/MSD/{name}/annotations/training"
val_root_annot_folder = f"data/MSD/{name}/annotations/validation"

for ind, image_path in enumerate(glob.glob(f"{tr_root_img_folder}/*.png")):
    if not os.path.exists(image_path.replace('images', 'annotations')):
        print(image_path, "does not have annotations")

for ind, image_path in enumerate(glob.glob(f"{val_root_img_folder}/*.png")):
    if not os.path.exists(image_path.replace('images', 'annotations')):
        print(image_path, "does not have annotations")
        os.remove(image_path)

for ind, image_path in enumerate(glob.glob(f"{tr_root_annot_folder}/*.png")):
    if not os.path.exists(image_path.replace('annotations', 'images')):
        print(image_path, "does not have image")
        os.remove(image_path)

for ind, image_path in enumerate(glob.glob(f"{val_root_annot_folder}/*.png")):
    if not os.path.exists(image_path.replace('annotations', 'images')):
        print(image_path, "does not have image")
        os.remove(image_path)
