import cv2

#读入图片
img = cv2.imread("1.png")

# 必须先转化成灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 寻找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 画出轮廓，-1,表示所有轮廓，画笔颜色为(0, 255, 0)，即Green，粗细为3
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# 显示图片
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.imshow("Contours", img)

# 等待键盘输入
cv2.waitKey(0)
cv2.destroyAllWindows()