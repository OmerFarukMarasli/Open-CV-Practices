import cv2
import numpy as np

img = cv2.imread("contour (1).png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
counturs,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = counturs[0]
area = cv2.contourArea(cnt)
print(area)
area_moments = cv2.moments(cnt)
print(area_moments["m00"])
len = cv2.arcLength(cnt,True)
print(len)