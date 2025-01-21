import cv2
import numpy as np
import matplotlib.pyplot as mpt

img=cv2.imread("../Temel-Islemler/Resimler/Robot.jpg")
kose=img[0:100,0:100]
koseyatay=img[0:100,0:250]

img[0:250,0:250]=(250,255,0)


cv2.imshow("Test",img)
cv2.imshow("Test2",kose)
cv2.imshow("Test1",koseyatay)
cv2.waitKey(0)
cv2.destroyAllWindows()