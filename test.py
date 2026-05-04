import cv2
img=cv2.imread('test.jpg')
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
#灰度图
gary=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gary",gary)
#
# #边缘检测
edges=cv2.Canny(gary,100,200)
cv2.imshow("edges",edges)



