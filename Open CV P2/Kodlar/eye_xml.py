import cv2
import numpy as np

img = cv2.imread("eye.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\frontalface.xml")
eyes = cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\eye.xml")

faces_cascade = faces.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces_cascade:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
    eyes_area = img[y:y+h,x:x+w]

eyes_cascade = eyes.detectMultiScale(eyes_area,1.2,3)
for (x,y,w,h) in eyes_cascade:
    cv2.rectangle(eyes_area,(x,y),(x+w,y+h),(255,0,0),5)



cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()