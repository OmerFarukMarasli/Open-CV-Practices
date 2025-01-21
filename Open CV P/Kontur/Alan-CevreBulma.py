import cv2

img = cv2.imread("\\ucgen.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,124,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contours[0])
cevre = cv2.arcLength(contours[0],True)
print(area)
print(cevre)