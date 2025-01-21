import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def findMaxCounters(counters):
    max_i =0
    max_contoursarea = 0
    for i in range(len(counters)):
        face_area = cv2.contourArea(counters)
        if face_area > max_contoursarea:
            max_contoursarea=face_area
            max_i = i

            try:
                c = max_contoursarea[max_i]
            except:
                max_contoursarea = [0]
                c=max_contoursarea[0]

while True:
    ret,frame = cap.read()
    roi = frame[200:350,400,500]
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower = np.array([0,45,79],dtype=np.uint8)
    upper = np.array([17,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv,lower,upper)
    kernel = np.ones((3,3),dtype=np.uint8)
    dilate = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(dilate,5)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >0 :
        c = findMaxCounters(contours)

        extLeft = tuple(c[c[:,:,0].argmin()][0])
        extRight = tuple(c[c[:,:,0].argmax()][0])
        extTop = tuple(c[c[:,:,1].argmax][0])
        extBot = tuple([c[c[:,:,1].argmin][0]])

        cv2.circle(frame,extLeft,5,(0,255,0),-1)
        cv2.circle(frame, extRight, 5, (0, 255, 0), -1)
        cv2.circle(frame, extTop, 5, (0, 255, 0), -1)
        cv2.circle(frame, extBot, 5, (0, 255, 0), -1)

        cv2.line(frame,extLeft,extTop,5,(0,255,0),2)
        cv2.line(frame, extTop, extBot, 5, (0, 255, 0), 2)
        cv2.line(frame, extBot, extRight, 5, (0, 255, 0), 2)






