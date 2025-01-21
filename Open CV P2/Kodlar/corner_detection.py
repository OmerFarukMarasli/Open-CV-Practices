import cv2
import numpy as np
img1 = cv2.imread("contour (1).png")
img2 = cv2.imread("text.png")
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corner = cv2.goodFeaturesToTrack(gray,50,0.01,9)
corner = np.int0(corner)
for conners in corner:
    x,y = conners.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)

cv2.imshow("pencere",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()