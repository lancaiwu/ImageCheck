# encoding: utf-8
from PIL import Image


def isYellow(pix):
    (r, g, b, max) = pix
    # print(r > 190 and g > 190 and b < 230)
    return r > 220 and g > 220 and b < 230


def parse():
    img = Image.open(r'C:\Users\Administrator.SKY-20170712YLK\Desktop\1111.png')
    img = img.crop((34, 28, 502, 297))
    pix = img.load()
    for t_x in range(img.size[0] - 1, 0, -1):
        for t_y in range(img.size[1], 10, -1):
            try:
                if abs(t_y - img.size[1]) > 10 and abs(t_x - img.size[0]) > 10 and isYellow(pix[t_x, t_y]) and isYellow(
                        pix[t_x, t_y - 5]) and isYellow(pix[t_x, t_y - 10]):
                    return t_x - 70 + 34
            except Exception:
                print "异常"


print parse()
