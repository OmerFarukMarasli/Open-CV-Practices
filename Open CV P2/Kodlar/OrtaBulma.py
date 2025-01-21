import cv2
import numpy as np

img = cv2.imread("contour (1).png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,tresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
M = cv2.moments(tresh)

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])
cv2.circle(img,(X,Y),6,(0,255,0),-1)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()