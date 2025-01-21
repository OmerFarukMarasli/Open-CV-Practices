import cv2
import numpy as np

img = cv2.imread("Resimler/car.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
haarcascade_car = cv2.CascadeClassifier("HaarCascad/car.xml")
cars = haarcascade_car.detectMultiScale(img_gray,1.1,2)
for(x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


