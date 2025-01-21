import cv2
import numpy as np

faces = cv2.imread("faces.jpg")
blur = cv2.blur(faces,(5,5))
gaussian_blur = cv2.GaussianBlur(faces,(3,3),cv2.BORDER_DEFAULT)
bilateral_blur = cv2.bilateralFilter(faces,5,75,75)
m_blur = cv2.medianBlur(faces,3)








cv2.imshow("Original",faces)
cv2.imshow("blur",blur)
cv2.imshow("gussian",gaussian_blur)
cv2.imshow("bilateral",bilateral_blur)
cv2.imshow("median",m_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
