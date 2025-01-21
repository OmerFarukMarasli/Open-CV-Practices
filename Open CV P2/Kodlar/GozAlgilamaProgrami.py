import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\behin\\Downloads\\eye_motion.mp4")


while True:
    ret,frame = cap.read()
    roi = frame[70:250,200:500]#y1,y2,x1,x2
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,5,255,cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)

        break


    cv2.imshow("thresh",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()