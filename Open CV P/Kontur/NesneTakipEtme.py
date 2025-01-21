import cv2
import numpy as np

cap=cv2.VideoCapture("\\dog.mp4")


while(True):
    _,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity=15
    lowerwhite=np.array([0,0,255-sensitivity])
    upperwhite=np.array([255,sensitivity,255])

    mask=cv2.inRange(hsv,lowerwhite,upperwhite)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(30) & 0xFF==ord("q"):

        break


cv2.destroyAllWindows()