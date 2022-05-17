import numpy as np
import shutil as sh
import os
from sklearn.model_selection import train_test_split


def get_files_from_folder(path):
    files = os.listdir(path)
    return np.asarray(files)


name = 'Task06_Lungs_RGB_2D_512_Balanced'

# Folder names
data_root = f"data/MSD/{name}"
tr_images_root = data_root + '/images/training/'
tr_images_bck_root = data_root + '/images/training_bck/'
tr_annotations_root = data_root + '/annotations/training/'
tr_annotations_bck_root = data_root + '/annotations/training_bck/'
val_images_root = data_root + '/images/validation/'
val_annotations_root = data_root + '/annotations/validation/'
# Move images to bck folder
if os.path.exists(tr_images_root):
    sh.move(tr_images_root, tr_images_bck_root)
elif not os.path.exists(tr_images_bck_root):
    raise Exception('No bck images folder found')
# Move images and annotations to bck folder
if os.path.exists(tr_annotations_root):
    sh.move(tr_annotations_root, tr_annotations_bck_root)
elif not os.path.exists(tr_annotations_bck_root):
    raise Exception('No bck annotations folder found')
# Create folders if not exist
os.makedirs(tr_images_root, exist_ok=True)
os.makedirs(tr_annotations_root, exist_ok=True)
os.makedirs(val_images_root, exist_ok=True)
os.makedirs(val_annotations_root, exist_ok=True)

# Load file names
images = get_files_from_folder(tr_images_bck_root)
annotations = get_files_from_folder(tr_annotations_bck_root)
# Train-Validation split
data_train, data_val, labels_train, labels_val = train_test_split(images, annotations,
                                                                  test_size=0.20,
                                                                  random_state=42)
# Move train images
for img in data_train:
    src = tr_images_bck_root+img
    dst = tr_images_root+img
    sh.copy(src, dst)
# Move train annotations
for img in labels_train:
    src = tr_annotations_bck_root+img
    dst = tr_annotations_root+img
    sh.copy(src, dst)

# Move val images
for img in data_val:
    src = tr_images_bck_root+img
    dst = val_images_root+img
    sh.copy(src, dst)
# Move val annotations
for img in labels_val:
    src = tr_annotations_bck_root+img
    dst = val_annotations_root+img
    sh.copy(src, dst)

print("Done!")
