import cv2
import numpy as np

img = cv2.imread("\\map.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
_,thresh = cv2.threshold(blur ,39,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))


