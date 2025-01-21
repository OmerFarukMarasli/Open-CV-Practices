import cv2
import face_recognition
import numpy as np
import face_recognition as fr

cap = cv2.VideoCapture("C:\\OpenCV_Udemy\\Face_recognation\\images\\face.jpg")
color = (0,255,0)
while True:
    ret,frame = cap.read()


    face_loc = fr.face_locations(frame)
    for index,loc in enumerate(face_loc):
        topy,botx,boty,topx = loc
        cv2.rectangle(frame,(topx,topy),(botx,boty),color)
        cv2.imshow("pencere", frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()