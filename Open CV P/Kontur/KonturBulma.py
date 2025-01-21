import cv2
import numpy as np

foto=cv2.imread("Resimler/contour1.png")
grifotograf=cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(grifotograf,124,255,cv2.THRESH_BINARY)
contur,ret=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(foto,contur,-1,(255,0,255),3)
cv2.imshow("Pencere",foto)
cv2.waitKey(0)
cv2.destroyAllWindows()