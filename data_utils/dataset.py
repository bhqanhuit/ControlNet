import json
import cv2
import numpy as np
import os
from torch.utils.data import Dataset
from PIL import Image
import random

def is_valid_image_pillow(file_name):
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False


# create paired file list

# class MyDataset(Dataset):
#     def __init__(self, opt):
#         self.data = {}
#         self.data_root = opt.data_root_dir

#         for root, dirs, files in os.walk(self.data_root):
#             for file in files:
#                 file_name = os.path.join(root, file)
#                 if (is_valid_image_pillow(file_name)):
#                     image_name = file_name.split('/')[-1].split('-')[0]
#                     try:
#                         self.data[image_name].append(file_name)
#                     except KeyError:
#                         self.data[image_name] = []
        
#         self.image_names = list(self.data.keys())
#         f = open("training/k-hair/pair_dataset.txt", "w")
#         for image_name in self.image_names:
            
#             print(len(self.data[image_name]))
#             for num in range(30):
#                 x = random.randint(0, len(self.data[image_name])-1)
#                 y = random.randint(0, len(self.data[image_name])-1)
#                 print(self.data[image_name][x], self.data[image_name][y])
#                 f.write(self.data[image_name][x] + " " + self.data[image_name][y] + "\n")
#         f.close()

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         return 0
    


class MyDataset(Dataset):
    def __init__(self, opt):
        self.data = []
        self.data_root = opt.data_root_dir

        f = open("training/k-hair/pair_dataset.txt", "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            self.data.append(line.strip())

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return 0
    
    