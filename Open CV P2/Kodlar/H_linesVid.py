import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\behin\\Desktop\\line.mp4")

while True:
    ret,frame = cap.read()
    cv2.namedWindow("Pencere",cv2.WINDOW_NORMAL)
    if ret ==False:
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv_lower = np.array([18,94,140],dtype=np.uint8)
    hsv_upper = np.array([48,255,255],dtype=np.uint8)
    mask = cv2.inRange(hsv,hsv_lower,hsv_upper)
    edges = cv2.Canny(mask,70,125)
    h_line = cv2.HoughLinesP(edges,1,np.pi/180,70,maxLineGap=200)
    for line in h_line:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),4)
    cv2.imshow("Pencere", frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()