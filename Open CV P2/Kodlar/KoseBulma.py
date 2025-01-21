import cv2
import numpy as np

img = cv2.imread("polygons.png",0)
_,tresh = cv2.threshold(img,240,255,cv2.THRESH_BINARY)
counters,_ = cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in counters:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    cv2.drawContours(img,[approx],-1,(0,255,0),2)
    if len(approx)==3:
        cv2.putText(img,"Ucgen",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0))
    elif len(approx)==4:
        cv2.putText(img, "Dortgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0))
    elif len(approx)==5:
        cv2.putText(img, "Besgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0))
    elif len(approx)==6:
        cv2.putText(img, "altigen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0))
    else:
        cv2.putText(img, "Elips", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0))
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()