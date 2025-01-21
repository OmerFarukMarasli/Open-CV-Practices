import cv2
import numpy as np

vid = cv2.VideoCapture("C:/Users/behin/Downloads/body.mp4")
bodycascasde  = cv2.CascadeClassifier("HaarCascad/fullbody (1).xml")

while True:
    ret,frame = vid.read()
    if ret ==False:
        break

    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = bodycascasde.detectMultiScale(frame_gray,1.4,4)
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Pencere",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
vid.release()
cv2.destroyAllWindows()