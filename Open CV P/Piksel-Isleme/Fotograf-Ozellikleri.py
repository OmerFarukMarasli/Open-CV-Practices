import cv2
import numpy as np
import matplotlib.pyplot as mlt

img=cv2.imread("Fotograf-Kaynaklari/Gul.jpg")
print("Yukseklik: {}".format(img.shape[0]))
print("Genişlik: {} ".format(img.shape[1]))
print("Kanal değeri: {}".format(img.shape[2]))
cv2.imshow("Fotograf1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()