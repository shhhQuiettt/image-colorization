import cv2
import numpy as np
import os
import glob

DATA_DIR = "data"

for dir in os.listdir(DATA_DIR):
    os.makedirs(os.path.join(DATA_DIR, dir, "gray"), exist_ok=True)
    os.makedirs(os.path.join(DATA_DIR, dir, "color"), exist_ok=True)
    for file in glob.glob(os.path.join(DATA_DIR, dir, "*.JPEG")):
        img = cv2.imread(file)
        img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        img_gray = img_lab[:, :, 0]

        img_color_filename = os.path.join(
            DATA_DIR, dir, "color", os.path.basename(file)
        )
        img_gray_filename = os.path.join(DATA_DIR, dir, "gray", os.path.basename(file))

        os.rename(file, img_color_filename)
        cv2.imwrite(img_gray_filename, img_gray)
