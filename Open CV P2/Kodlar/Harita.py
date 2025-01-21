import cv2
import numpy as np

img = cv2.imread("map (1).jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
counters,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull = []
for i in range(len(counters)):
    hull.append(cv2.convexHull(counters[i],False))

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),dtype=np.uint8)
for i in range(len(counters)):
    cv2.drawContours(bg,counters,i,(0,255,0),3,8,hier)
    cv2.drawContours(bg,hull,i,(255,0,0),3)
cv2.imshow("pencere",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()