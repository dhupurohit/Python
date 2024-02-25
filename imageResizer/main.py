import cv2

src = "1C.jpg"
des = "1C1-Resize.png"
per = 150

img = cv2.imread(src, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", img)

width = int(img.shape[1] * per / 100)
height = int(img.shape[0] * per / 100)

output = cv2.resize(img, (width,height))

cv2.imwrite(des, output)
# cv2.waitKey(0)