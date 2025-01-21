import cv2
import numpy as np


img =cv2.imread("para.jpg",0)
img = cv2.medianBlur(img,5)
circle = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=5,maxRadius=30)
if circle is not None:
    circle = np.uint16(np.around(circle))
    for i in circle[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),1)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()