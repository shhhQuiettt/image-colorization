import torchvision.transforms as T
from PIL import Image
import random
import os
import glob

random.seed(0xC0FFEE)
DATA_PATH = "data"
TEST_SPLIT = 0.1
VALIDATION_SPILT = 0.2

files = glob.glob(os.path.join(DATA_PATH, "*.JPEG"))

no_of_test_files = int(TEST_SPLIT * len(files))

no_of_validation_files = (len(files) - no_of_test_files) * VALIDATION_SPILT
no_of_train_files = len(files) - no_of_test_files - no_of_validation_files

random.shuffle(files)

test_files = files[:no_of_test_files]
validation_files = files[no_of_test_files : no_of_test_files + no_of_validation_files]
train_files = files[no_of_test_files + no_of_validation_files :]

os.makedirs(os.path.join(DATA_PATH, "val"), exist_ok=True)
os.makedirs(os.path.join(DATA_PATH, "train"), exist_ok=True)
os.makedirs(os.path.join(DATA_PATH, "train"), exist_ok=True)

for file in validation_files:
    os.rename(file, os.path.join(DATA_PATH, "val", os.path.basename(file)))

for file in train_files:
    os.rename(file, os.path.join(DATA_PATH, "train", os.path.basename(file)))

for file in test_files:
    os.rename(file, os.path.join(DATA_PATH, "test", os.path.basename(file)))
