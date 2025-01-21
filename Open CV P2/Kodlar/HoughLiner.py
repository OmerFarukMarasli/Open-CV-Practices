import cv2
import numpy as np

img = cv2.imread("h_line.png",0)
edges = cv2.Canny(img,70,125)
h_lines = cv2.HoughLinesP(edges,1,np.pi/180,40,maxLineGap=200)
for line in h_lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
