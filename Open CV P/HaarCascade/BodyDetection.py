import cv2
import numpy as np



img = cv2.imread("Resimler/body (1).jpg")
body_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
body_cascade = cv2.CascadeClassifier("HaarCascad/fullbody (1).xml")
bodies = body_cascade.detectMultiScale(body_gray,1.1,2)
for(x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()