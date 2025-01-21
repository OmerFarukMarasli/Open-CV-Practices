import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_or = cv2.bitwise_or(img1,img2)
cv2.imshow("bitwise",bit_or)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()