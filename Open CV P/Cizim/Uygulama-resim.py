import cv2
import numpy as np

def bos():
    pass


tablo=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("foto")

cv2.createTrackbar("R","foto",0,255,bos)
cv2.createTrackbar("G","foto",0,255,bos)
cv2.createTrackbar("B","foto",0,255,bos)
cv2.createTrackbar("0=KAPAT  & 1=ACIK","foto",0,1,bos)

while True:
    cv2.imshow("foto",tablo)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    r=cv2.getTrackbarPos("R","foto")
    g=cv2.getTrackbarPos("G","foto")
    b=cv2.getTrackbarPos("B","foto")
    an=cv2.getTrackbarPos("0=KAPAT  & 1=ACIK","foto")

    if cv2.getTrackbarPos("0=KAPAT  & 1=ACIK","foto")==0:
        tablo[:]=[0,0,0]
    if cv2.getTrackbarPos("0=KAPAT  & 1=ACIK","foto")==1:
        tablo[:] = [b, g, r]

cv2.destroyAllWindows()

