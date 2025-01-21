import cv2
import numpy as np


cap = cv2.VideoCapture("D:\\OpenCV\\Resimler\\faces.mp4")
face_cascade= cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\frontalface.xml")

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    facess = face_cascade.detectMultiScale(gray,1.4,1)

    for (x,y,w,h) in facess:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.imshow("Pencere", frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
         break
cap.release()
cv2.destroyAllWindows()