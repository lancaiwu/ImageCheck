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
img2 = Image.open(agr2)
img2 = img2.crop(box)
img3 = ImageChops.difference(img1, img2)

img = np.array(img3.convert('RGB'))

endCol = 0
rows, cols, colors = img.shape
isOk = False
for j in range(0, cols)[::-1]:
    if isOk:
        break
    for i in range(0, rows)[::-1]:
        if isOk:
            break
        for color in range(0, colors)[::-1]:
            if isOk:
                break
            # print "j %d i %d  c %d  color %d" % (j, i, color,img[i, j, color])
            if img[i, j, color] > 80:
                endCol = 56 + j
                isOk = True
                break
        if isOk:
            break
    if isOk:
        break

print endCol
