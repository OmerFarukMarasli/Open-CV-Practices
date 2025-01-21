import cv2
import numpy as np

cap = cv2.VideoCapture("C://Users//behin//Desktop//cap.mp4")
while True:
    ret,frame = cap.read()
    if ret==False:
        break
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.waitKey(20)
    cv2.imshow("Pencere",frame)
cap.release()
cv2.destroyAllWindows()