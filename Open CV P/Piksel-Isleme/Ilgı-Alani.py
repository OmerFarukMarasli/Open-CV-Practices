import cv2
import numpy as np
import matplotlib.pyplot as mpl

img=cv2.imread("Fotograf-Kaynaklari/Basketbol.jpg")
ilgialan=img[0:250,0:250]
cv2.imshow("Foto1",img)
cv2.imshow("Foto2",ilgialan)
cv2.waitKey(0)
cv2.destroyAllWindows()