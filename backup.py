# encoding: utf-8
from PIL import Image
import ImageChops
import numpy as np
import sys

age1 = sys.argv[1]
agr2 = sys.argv[2]

box = (56, 140, 665, 550)
img1 = Image.open(age1)
img1 = img1.crop(box)
#img1.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\111.jpg')
img2 = Image.open(agr2)
img2 = img2.crop(box)
#img2.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\222.jpg')
img3 = ImageChops.difference(img1, img2)
#img3.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\3.jpg')

img = np.array(img3.convert('RGB'))

endCol = 0
rows, cols, colors = img.shape
for j in range(cols):
    for i in range(rows):
        for color in range(colors):
            if img[i, j, color] > 80:
                endCol = 56 + j
                # print("列 %d  行 %d ，,color %d , color %d " % (56 + j, 140 + i, color, img[i, j, color]))

print endCol
