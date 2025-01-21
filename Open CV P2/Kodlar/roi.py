import cv2
import numpy as np


def bos(x):
    pass

canvas = np.ones((512,512,3),np.uint8)
cv2.namedWindow("canvas")
cv2.createTrackbar("R","canvas",0,255,bos)
cv2.createTrackbar("G","canvas",0,255,bos)
cv2.createTrackbar("B","canvas",0,255,bos)
cv2.createTrackbar("switch","canvas",0,1,bos)

while True:
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

    r = cv2.getTrackbarPos("R","canvas")
    g = cv2.getTrackbarPos("G","canvas")
    b = cv2.getTrackbarPos("B","canvas")
    s = cv2.getTrackbarPos("switch","canvas")


    if s == 0:
        canvas[:] = [0,0,0]
    elif s ==1:
        canvas[:] = [r, g, b]
    cv2.imshow("canvas", canvas)

cv2.destroyAllWindows()