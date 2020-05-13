import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"OpenCV\Images\Kose.jpg",cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

koseler = cv2.goodFeaturesToTrack(gray,50,0.01,10)
koseler = np.int0(koseler)

for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Corner',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
