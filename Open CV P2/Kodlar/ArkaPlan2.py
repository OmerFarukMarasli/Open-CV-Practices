import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\behin\\Downloads\\car.mp4")
subs = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=False)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    mask = subs.apply(frame)
    cv2.imshow("pencere",mask)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()