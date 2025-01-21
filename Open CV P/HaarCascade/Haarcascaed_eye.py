import cv2
import numpy as np

img = cv2.imread("Resimler/face.png")
haarcascade_face = cv2.CascadeClassifier("/haarcascade_frontaleye.xml")
haarcascade_eye = cv2.CascadeClassifier("HaarCascad/haarcascade_eye.xml")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = haarcascade_face.detectMultiScale(img_gray,1.5,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

gray2 = img_gray[y:y+h, x:x+w]
img2 = img[y:y+h,x:x+w]
eyes = haarcascade_eye.detectMultiScale(gray2,1.5,5)
for(xe,ye,we,he) in eyes:
    cv2.rectangle(img2,(xe,ye),(xe+we,ye+he),(0,0,255),2)
cv2.imshow("Pencere",img)
while True:
    if cv2.waitKey(0) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()