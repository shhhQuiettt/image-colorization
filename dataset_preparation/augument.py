import os
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import glob
import cv2
import torchvision.transforms as T
import albumentations as A
import random

random.seed(0xC0FFEE)

TRAIN_DATA = "data/train"

augumentation_pipeline = A.Compose([A.HorizontalFlip(p=1), A.Rotate(limit=15, p=0.9)])

train_files = glob.glob(os.path.join(TRAIN_DATA, "*.JPEG"))
for file in train_files:
    image = cv2.imread(file)
    image = augumentation_pipeline(image=image)["image"]
    filename = os.path.splitext(file)[0] + "_aug" + os.path.splitext(file)[1]

    cv2.imwrite(filename, image)
