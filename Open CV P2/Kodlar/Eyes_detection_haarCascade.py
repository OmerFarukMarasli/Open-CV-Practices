import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\behin\\Downloads\\eyes.mp4")

face_cascade = cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\eye.xml")

while True:
    ret,frame = cap.read()
    if ret ==False:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        eyes_area = frame[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(eyes_area,1.1,2)
    for (x,y,w,h) in eyes:
        cv2.rectangle(eyes_area,(x,y),(x+w,y+h),(255,0,0),5)
    cv2.imshow("Pencere",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


