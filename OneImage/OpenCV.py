from flask import Flask
from flask import jsonify, render_template
from matplotlib.pyplot import imsave

app = Flask(__name__)
import base64
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image

# 读入图片4
img = cv2.imread("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\1.png")
# 必须先转化成灰度图
hgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(hgray, 127, 255, cv2.THRESH_BINARY)

# 寻找轮廓v
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 画出轮廓，-1,表示所有轮廓，画笔颜色为(0, 255, 0)，即Green，粗细为3
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for c in contours:
    # 现计算出一个简单的边界框
    x, y, w, h = cv2.boundingRect(c)  # 将轮廓信息转换成(x, y)坐标，并加上矩形的高度和宽度
    # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)  # 画出矩形
    #计算包围目标的最小矩形区域
    # rect = cv2.minAreaRect(c)
    # box = cv2.boxPoints(rect)
    # box =np.int0(box)
    # # 注：OpenCV没有函数能直接从轮廓信息中计算出最小矩形顶点的坐标。所以需要计算出最小矩形区域，
    # # 然后计算这个矩形的顶点。由于计算出来的顶点坐标是浮点型，但是所得像素的坐标值是整数（不能获取像素的一部分），
    # # 所以需要做一个转换
    # # draw contours
    # cv2.drawContours(img, [box], 0, (0, 0, 255), 3)  # 画出该矩形

    # calculate center and radius of minimum enclosing circle
    # (x, y), radius = cv2.minEnclosingCircle(c)  # 会返回一个二元组，第一个元素为圆心的坐标组成的元组，第二个元素为圆的半径值。
    # # cast to integers
    # center = (int(x), int(y))
    # radius = int(radius)
    # # draw the circle
    # img = cv2.circle(img, center, radius, (0, 255, 0), 2)

# 显示图片
# cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
# cv2.imshow("Contours", img)

# 等待键盘输入
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\2342342.jpg",img)
cv2.imwrite("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\44.jpg", img)
