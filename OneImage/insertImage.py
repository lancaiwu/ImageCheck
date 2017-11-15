# encoding: utf-8
import time
from PIL import Image
from PIL import ImageChops
import numpy as np
import sys
import pymysql

xLeftOffset = 56
yTopOffset = 290
xRightOffset = 680
yBottomOffset = 650

box = (xLeftOffset, yTopOffset, xRightOffset, yBottomOffset)

#  原图
agr2 = r"C:\Users\Administrator.SKY-20170712YLK\Desktop\screen\yuantu\199.jpg"

img2 = Image.open(agr2)
img2 = img2.crop(box)
imgRgb2 = np.array(img2.convert('RGB'))
#img2.save(r"C:\Users\Administrator.SKY-20170712YLK\Desktop\qie1222222.jpg")
#  获取  四个 点 的像素 / 左上、右上、右下、左下 分别是 +10

img2LeftTop = imgRgb2[10, 10, 0]
img2RightTop = imgRgb2[10, xRightOffset - xLeftOffset - 10, 0]
img2RightBottom = imgRgb2[yBottomOffset - yTopOffset - 10, xRightOffset - xLeftOffset - 10, 0]
img2LeftBottom = imgRgb2[yBottomOffset - yTopOffset - 10, 10, 0]

# 打开数据库连接
#db = pymysql.connect("121.201.67.82", "root", "zyy.@!", "gc")
db = pymysql.connect("127.0.0.1", "root", "123456", "gc")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 插入
agr2=agr2.replace("\\","\\\\\\")
sql='INSERT INTO t_yz_img(img_name,img_path,img_left_top,img_right_top,img_right_bottom,img_left_bottom,time) VALUES (%s,%s,%d,%d,%d,%d,%d)' % (r"'"+'bingshan'+"'",r"'"+agr2+"'", img2LeftTop, img2RightTop, img2RightBottom, img2LeftBottom, time.time())
cursor.execute(sql)
db.commit()
# 关闭数据库连接
db.close()
