import os
import sys
import glob

img_list = glob.glob("/home/ycliu/Retinaface/data/Market-1501-v15.09.15/query/*.jpg")

with open("./Market1501.txt", 'w') as rf:
    for img_path in img_list:
        img_name = img_path.split('/')[-1]
        rf.write(img_name+'\n')

