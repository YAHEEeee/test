import cv2

#读取图片
img=cv2.imread(r"/image_proscessing_basics/test.jpg")
#灰度转换
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img[0,0])       #原图像素
print(gray[0,0])       #灰度值

#边缘检测
edges=cv2.Canny(gray,100,200)

#保存结果
cv2.imwrite("result/gray.png",gray)
cv2.imwrite("result/edges.png",edges)

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
