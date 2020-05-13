import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"OpenCV\Images\resim1.jpg",cv2.IMREAD_COLOR)


px=img[100:200,100:200]=[0,0,0]
img[100:200,100:200]=[0,0,0]




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
