import cv2
import numpy as np

tuval1 = np.zeros((512,512,3),np.uint8)+255
tuval2 = np.zeros((512,512,3),np.uint8)+255
cv2.circle(tuval1,(256,256),60,(255,0,0),-1)
cv2.rectangle(tuval2,(150,150),(350,350),(0,0,255),-1)
add = cv2.add(tuval1,tuval2)


dst = cv2.addWeighted(tuval1,0.2,tuval2,0.8,0)
cv2.imshow("tuval1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()