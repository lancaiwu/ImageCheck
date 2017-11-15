# encoding: utf-8
# ! python2.7
from PIL import Image
import ImageChops
import numpy as np
import sys

class Check:
    imagePath1 = ""
    imagePath2 = ""

    def __init__(self, image1, image2):
        self.imagePath2 = image1
        self.imagePath1 = image2
        print self.imagePath1
        print self.imagePath2
        self.startCheck()

    def startCheck(self):
        print "dfdsf222"
        box = (56, 140, 665, 550)
        img1 = Image.open(self.imagePath1)
        img1 = img1.crop(box)
        img1.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\111.jpg')
        img2 = Image.open(self.imagePath1)
        img2 = img2.crop(box)
        img2.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\222.jpg')
        img3 = ImageChops.difference(img1, img2)
        img3.save(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\3.jpg')
        img = np.array(img3.convert('RGB'))
        rows, cols, colors = img.shape
        # for j in range(cols):
        #     for i in range(rows):
        #         for color in range(colors):
        #             print("列 %d  行 %d ，,color %d , color %d " % (56 + j, 140 + i, color, img[i, j, color]))
                    # if img[i, j, color] > 80:
                    #    print "%d" % (56 + j)
                    #    print("列 %d  行 %d ，,color %d , color %d " % (56 + j, 140 + i, color, img[i, j, color]))


if __name__ == "__main__":
    Check(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\1.jpg',
          r'C:\Users\Administrator.SKY-20170712YLK\Desktop\2.jpg')

else:
    age1 = sys.argv[1]
    agr2 = sys.argv[2]
    Check(age1, agr2)
    print sys.version
    print sys.version_info
    # print imagePath1
    # print imagePath2
    # print "dfdfsd"
