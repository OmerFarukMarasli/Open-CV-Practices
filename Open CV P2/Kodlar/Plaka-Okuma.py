import cv2
import numpy as np
import pandas as pd
import pytesseract as pt
import imutils

img = cv2.imread("araba.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(gray,2,120,255)
edged = cv2.Canny(filtered,120,240)
contours,_ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours(contours)
cnt = sorted(cnt,key=cv2.contourArea,revers=True)[:,10]
screen = None

for cnts in cnt:
    epsilon = 0.018*cv2.arcLength(cnts,closed=True)
    approx = cv2.approxPolyDP(cnts,epsilon,closed=True)
    if len(approx) ==4:
        screen = approx

mask = np.zeros(img.shape,np.uint8)
new_image = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
new_image = cv2.bitwise_and(img,img,mask=mask)


(x,y) = np.where(mask = 255)
(xmax,ymax) = (np.min(x),np.min(y))
(xbuttom,ybuttom) =(np.max(x),np.max(y))
corped = img[xmax:xbuttom+1,ymax:ybuttom+1]
text = pt.image_to_string(corped)
print(text)





cv2.imshow("pencre",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()