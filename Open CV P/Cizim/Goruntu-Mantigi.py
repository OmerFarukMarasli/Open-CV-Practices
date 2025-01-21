import cv2
import numpy as np

canvas=np.zeros((39,39,3),dtype=np.uint8)
canvas[0,1]=(255,255,255)
canvas[0,2]=(255,255,199)
canvas[1,14]=(255,255,1)
canvas=cv2.resize(canvas,(750,750),interpolation=cv2.INTER_AREA)


cv2.imshow("Tablo",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()