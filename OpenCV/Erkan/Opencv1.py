import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"OpenCV\Images\resim1.jpg",cv2.IMREAD_COLOR)
print("Renkli",img.shape)
print("Renkli",img[200][200])
cv2.imshow("image",img)

#---------------------------------------
imgBW=cv2.imread(r"OpenCV\")


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
