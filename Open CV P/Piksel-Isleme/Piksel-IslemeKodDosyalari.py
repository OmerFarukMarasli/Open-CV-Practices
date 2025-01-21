import cv2
import numpy

img=cv2.imread("../Temel-Islemler/Resimler/Robot.jpg")

#pixelrengi=img[10,10]
#print(pixelrengi)

#(b,g,r)=img[50,100]
#print("(0,0) - Red: {},Green: {},Blue: {}".format(r,g,b))

#BGR

#b=img[100,100,0]
#g=img[100,100,1]
#r=img[100,100,2]
#print("Önceki Değerler: ",img[100,100])
#img[100,100]=[20,20,20]
#print("Sonraki Değerler: ",img[100,100])
print("Önceki Değerler>: ",img.item(100,100,0))
img.itemset((100,100,0),82)
print("Sonraki Değer>: ",img.item(100,100,0))
