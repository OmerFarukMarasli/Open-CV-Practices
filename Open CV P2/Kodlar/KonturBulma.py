import cv2
import numpy as np

img = cv2.imread("C:\\Users\\behin\\Downloads\\contour1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
counters,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,counters,-1,(0,255,0),3)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()