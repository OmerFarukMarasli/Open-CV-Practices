import cv2
import numpy as np

img = cv2.imread("Resimler/face.png")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
haarcascade_face = cv2.CascadeClassifier("HaarCascad/frontalface.xml")
faces = haarcascade_face.detectMultiScale(img_gray,1.6,10)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Pencere",img)


while True:
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()