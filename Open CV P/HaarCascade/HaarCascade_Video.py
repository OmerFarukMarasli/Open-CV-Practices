import cv2
import numpy as np

cap = cv2.VideoCapture("/faces.mp4")
haarcascade_faces = cv2.CascadeClassifier("HaarCascad/frontalface.xml")

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = haarcascade_faces.detectMultiScale(frame_gray,3,3)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Pencere",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()
