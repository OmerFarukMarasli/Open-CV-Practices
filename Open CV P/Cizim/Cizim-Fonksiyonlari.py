import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8)+88

cv2.imshow("Siyah Tuval",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()