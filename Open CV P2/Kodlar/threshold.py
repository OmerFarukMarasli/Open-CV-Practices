import cv2
import numpy as np

kernel = np.ones((10,10),dtype=np.uint8)
img = cv2.imread("Basketbol-Boyu-Uzatir-Mi.jpg",0)
erosion = cv2.erode(img,kernel,iterations=2)
dilate = cv2.dilate(img,kernel,iterations=1)
morp = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("penceer",morp)
cv2.waitKey(0)
cv2.destroyAllWindows()