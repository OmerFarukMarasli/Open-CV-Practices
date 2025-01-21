import cv2
import numpy as np
import matplotlib.pyplot as mpl

img=cv2.imread("Fotograf-Kaynaklari/OpenCVlogo1.png")
print("Shape{}".format(img.shape))

(B,G,R)=cv2.split(img)
merged=cv2.merge([B,G,R])


"""
cv2.namedWindow("OpenCV",cv2.WINDOW_NORMAL)
cv2.namedWindow("OpenCV-B",cv2.WINDOW_NORMAL)
cv2.namedWindow("OpenCV-G",cv2.WINDOW_NORMAL)

cv2.namedWindow("Merged",cv2.WINDOW_NORMAL)
cv2.imshow("Merged",merged)
cv2.imshow("OpenCV",img)
cv2.imshow("OpenCV-B",B)
cv2.imshow("OpenCV-G",G)
"""

karaekran=np.zeros(img.shape[:2],dtype="uint8")

cv2.imshow("OpenCV-R",cv2.merge([karaekran,karaekran,R]))
cv2.imshow("OpenCV-B",cv2.merge([B,karaekran,karaekran]))
cv2.imshow("OpenCV-G",cv2.merge([karaekran,G,karaekran]))

cv2.waitKey(0)
cv2.destroyAllWindows()