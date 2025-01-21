import cv2
import numpy as np

img = cv2.imread("body (1).jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier("D:\\OpenCV\\HaarCascade\\fullbody.xml")

body = body_cascade.detectMultiScale(gray,1.2,1)
for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()