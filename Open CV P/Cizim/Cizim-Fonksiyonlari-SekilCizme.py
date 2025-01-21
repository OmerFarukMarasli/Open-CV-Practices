import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255
"""
#cv2.namedWindow("Ekran-Ismi",cv2.WINDOW_NORMAL)
print(canvas)
cv2.line(canvas,(100,100),(255,255),(100,100,100),thickness=5)
#cv2.rectangle(canvas,(100,199),(255,15),(255,19,255),thickness=100)
cv2.circle(canvas,(100,199),29,(0,0,0),thickness=-1)
n1=(100,199)
n2=(20,100)
n3=(299,100)
cv2.line(canvas,n1,n2,(255,0,255),4)
cv2.line(canvas,n2,n3,(0,255,255),4)
cv2.line(canvas,n1,n3,(255,255,0),4)
"""
noktalar=np.array([[[0,0],[0,500],[500,0],[500,500]]],np.int32)
cv2.polylines(canvas,[noktalar],True,(255,0,255),3)
cv2.ellipse(canvas,(100,233),(120,200),20,0,360,(0,0,255),3)

cv2.imshow("Ekran-Ismi",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
