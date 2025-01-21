import cv2
import numpy as np


vid = cv2.VideoCapture("/eye.mp4")
facehaar_cascade = cv2.CascadeClassifier("HaarCascad/frontalface.xml")
eyehaar_cascade = cv2.CascadeClassifier("HaarCascad/haarcascade_eye.xml")

while True:
    ret,frame = vid.read()
    if ret == False:
        break
    frame = cv2.resize(frame,(480,360))
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facehaar_cascade.detectMultiScale(gray_frame,1.5,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    roi_area = frame[y:y+h,x:x+w]
    roi_area_gray = gray_frame[y:y+h,x:x+w]
    eyes = eyehaar_cascade.detectMultiScale(roi_area_gray,1.1,2)
    for(xe,ye,we,he) in eyes:
        cv2.rectangle(roi_area,(xe,ye),(xe+we,ye+he),(0,0,255),3)
    cv2.imshow("Pencere",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()