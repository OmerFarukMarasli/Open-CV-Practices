import cv2
import numpy as np

canvas=np.zeros((1000,20000,3),dtype=np.uint8)

font1=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(canvas,"OMER-FARUK-MARASLI",(100,100),font1,5,(255,0,255),cv2.LINE_AA)








cv2.putText(canvas,"aalşsdjf",(100,122),font1,3,(100,199,100),cv2.LINE_AA)




cv2.imshow("Çizim ekranı",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()