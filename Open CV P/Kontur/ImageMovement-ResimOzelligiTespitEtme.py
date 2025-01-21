import cv2

img=cv2.imread("Resimler/ucgen.jpeg")
griucgen=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(griucgen,127,255,cv2.THRESH_BINARY)
M=cv2.moments(thresh)
X=int(M["m10"]/M["m00"])
Y=int(M["m01"]/M["m00"])
cv2.circle(img,(X,Y),5,(255,255,255),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

