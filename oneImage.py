# encoding: utf-8
from PIL import Image
import ImageChops
import numpy as np
import sys

box = (56, 270, 685, 640)
# box = (262, 300, 325, 380)
# img1 = Image.open(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\4.jpg')

#box = (262, 300, 325, 380)
img1 = Image.open(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\4.jpg')
img1 = img1.crop(box)
img1.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\213.jpg')
c = img1.convert('L')
c.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\2223.jpg')
imageColor = np.array(c)
rows, cols = imageColor.shape
max = 0
min = 259
for i in range(rows):  # x
    count = 0
    for j in range(cols):  # y
        # for color in range(colors):
        print "%d列,%d行%d  %d" % (j + 56, i + 270, 0, imageColor[i, j])
        # if imageColor[i, j] <= 100 and imageColor[i, j] >= 40:
        #     count = count + 1
        #     if max < imageColor[i, j]:
        #         max = imageColor[i, j]
        #     if min > imageColor[i, j]:
        #         min = imageColor[i, j]
        #     if count > 97:
        #         count = 0
        #         # print i
        #         print "%d列,%d行%d  %d" % (j + 56, i + 270, 0, imageColor[i, j])
        # else:
        #     count = 0
# print max
# print min
