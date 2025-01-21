import cv2
import numpy as np

img = cv2.imread("bitwise_2.png",0)
cols,rows = img.shape
m = cv2.getRotationMatrix2D((cols/3,rows/3),90,1)
dst = cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("pencere",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()