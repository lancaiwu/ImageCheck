# encoding: utf-8
from PIL import Image
import ImageChops
import numpy as np
import time

box = (56, 140, 665, 550)
img1 = Image.open(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\1111.png')
img1 = img1.crop(box)
# img1.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\111.jpg')
img2 = Image.open(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\2222.png')
img2 = img2.crop(box)
# img2.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\222.jpg')
img3 = ImageChops.difference(img1, img2)
img3.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\3333.jpg')

img = np.array(img3.convert('RGB'))

rows, cols, colors = img.shape
isOk = False
for j in range(0, cols, 1)[::-1]:
    if isOk:
        break
    for i in range(0, rows, 10)[::-1]:
        if isOk:
            break
        # for color in range(0, colors)[::-1]:
        #     if isOk:
        #         break
        #     if img[i, j, color] > 80:
        #         print "j %d i %d  c %d  color %d" % (j, i, color, img[i, j, color])
        #         endCol = 56 + j
        #         isOk = True
        #         break
        if img[i, j, 0] > 80:
            endCol = 56 + j
            isOk = True
            break
    if isOk:
        break
print endCol
