# encoding: utf-8
from PIL import Image
from PIL import ImageChops
import numpy as np
import sys
import pymysql
import time


# 插入 记录
def insertRecord(db, uid, phoneNumber, imagePath1, imagePath2, checkResultType, checkResult, time):
    if imagePath1 is not None:
        imagePath1 = imagePath1.replace("\\", "\\\\\\")
    else:
        imagePath1 = ""
    if imagePath2 is not None:
        imagePath2 = imagePath2.replace("\\", "\\\\\\")
    else:
        imagePath2 = ""
    sql = "INSERT INTO t_yz_record(phoneNumber, uid, imagePath1, imagePath2, checkResultType, checkResult, time) VALUE (%s,%s,%s,%s,%d,%d,%d)" % (
        str(phoneNumber), str(uid), r"'" + imagePath1 + "'", r"'" + imagePath2 + "'", checkResultType, checkResult, time)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    return


xLeftOffset = 56
yTopOffset = 290
xRightOffset = 680
yBottomOffset = 650

box = (xLeftOffset, yTopOffset, xRightOffset, yBottomOffset)

agr2 = sys.argv[1]
phoneNumber = sys.argv[2]
uid = sys.argv[3]
#  验证图
# agr2 = "C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\screen\\175.jpg"
# phoneNumber = "15712007777"  # 手机号
# uid = 1  # uid
time = time.time()  # 日期
img_path = None  # 原图
checkResultType = -1  # 结果类型

img2 = Image.open(agr2)
img2 = img2.crop(box)
imgRgb2 = np.array(img2.convert('RGB'))
# img2.save("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\qie1222222.jpg")
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

offset = 20

selectImgSql = "select * from t_yz_img where img_left_top>%d and img_left_top<%d and  img_right_top>%d and img_right_top<%d  and  img_right_bottom>%d and img_right_bottom<%d and img_left_bottom>%d and img_left_bottom<%d " % (
    img2LeftTop - offset, img2LeftTop + offset, img2RightTop - offset, img2RightTop + offset, img2RightBottom - offset,
    img2RightBottom + offset, img2LeftBottom - offset, img2LeftBottom + offset)

try:
    # 执行sql语句
    cursor.execute(selectImgSql)
    # 使用 fetchone() 方法获取单条数据 .results = cursor.fetchall() 所有数据
    # 获取所有记录列表
    results = cursor.fetchone()
    if results is not None:
        img_path = results[2]
        #print("原图路径:%s" % (img_path))
        # for row in results:
        #     img_path = row[2]
        #     print("原图路径:%s" % (img_path))

except:
    checkResultType = -1
# finally:
# 关闭数据库连接
# db.close()

endCol = 0

if img_path is not None:
    # 原图
    age1 = img_path

    img1 = Image.open(age1)
    img1 = img1.crop(box)
    imgRgb1 = np.array(img1.convert('RGB'))
    # img1.save("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\qie1111111.jpg")

    img1LeftTop = imgRgb1[10, 10, 0]
    img1RightTop = imgRgb1[10, xRightOffset - xLeftOffset - 10, 0]
    img1RightBottom = imgRgb1[yBottomOffset - yTopOffset - 10, xRightOffset - xLeftOffset - 10, 0]
    img1LeftBottom = imgRgb1[yBottomOffset - yTopOffset - 10, 10, 0]

    img3 = ImageChops.difference(img1, img2)
    paths = age1.split("/")
    filename = paths[len(paths) - 1].split(".")[0]
    # filennn = "C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\44444.jpg"
    # img3.save(filennn)
    #img3.show()
    img = np.array(img3.convert('RGB'))

    rows, cols, colors = img.shape
    isOk = False
    num = 0
    for j in range(0, cols)[::-1]:
        if isOk and num > 90:
            checkResultType = 0
            break
        for i in range(0, rows)[::-1]:
            if isOk and num > 90:
                checkResultType = 0
                break
            for color in range(0, colors)[::-1]:
                if isOk and num > 90:
                    checkResultType = 0
                    break

                # 红
                if img[i, j, 0] > 50:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                # 绿
                if img[i, j, 1] > 50:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                # 蓝
                if img[i, j, 2] > 50:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                num = 0

                # # print "j %d i %d  c %d  color %d" % (j, i, color,img[i, j, color])
                # if img[i, j, color] > 50:
                #     endCol = 56 + j
                #     isOk = True
                #     num = num + 1
                #     continue
                # else:
                #     num = 0
            collls = i
            if isOk and num > 90:
                checkResultType = 0
                break
        if isOk and num > 90:
            checkResultType = 0
            break

if img_path is not None and endCol > 0 and endCol < 140:
    # 原图
    img1 = Image.open(age1)
    img1 = img1.crop(box)
    imgRgb1 = np.array(img1.convert('RGB'))
    # img1.save("C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\qie1111111.jpg")

    img1LeftTop = imgRgb1[10, 10, 0]
    img1RightTop = imgRgb1[10, xRightOffset - xLeftOffset - 10, 0]
    img1RightBottom = imgRgb1[yBottomOffset - yTopOffset - 10, xRightOffset - xLeftOffset - 10, 0]
    img1LeftBottom = imgRgb1[yBottomOffset - yTopOffset - 10, 10, 0]

    img3 = ImageChops.difference(img1, img2)
    paths = age1.split("/")
    filename = paths[len(paths) - 1].split(".")[0]
    # filennn = "C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\44444.jpg"
    # img3.save(filennn)
    # img3.show()
    img = np.array(img3.convert('RGB'))

    rows, cols, colors = img.shape
    isOk = False
    num = 0
    for j in range(0, cols)[::-1]:
        if isOk and num > 90:
            checkResultType = 0
            break
        for i in range(0, rows)[::-1]:
            if isOk and num > 90:
                checkResultType = 0
                break

            # 红
            if img[i, j, 0] > 10:
                endCol = 56 + j
                isOk = True
                num = num + 1
                continue

            # 绿
            if img[i, j, 1] > 10:
                endCol = 56 + j
                isOk = True
                num = num + 1
                continue

            # 蓝
            if img[i, j, 2] > 10:
                endCol = 56 + j
                isOk = True
                num = num + 1
                continue

            num = 0

            # for color in range(0, colors)[::-1]:
            #     if isOk and num > 90:
            #         break
            #     # print "j %d i %d  c %d  color %d" % (j, i, color,img[i, j, color])
            #     if img[i, j, color] > 10:
            #         endCol = 56 + j
            #         isOk = True
            #         num = num + 1
            #         continue
            #     else:
            #         num = 0
            # collls = i
            if isOk and num > 90:
                checkResultType = 0
                break
        if isOk and num > 90:
            checkResultType = 0
            break

insertRecord(db, uid, phoneNumber, img_path, agr2, checkResultType, endCol, time)
# 关闭数据库连接
db.close()

print(endCol)
