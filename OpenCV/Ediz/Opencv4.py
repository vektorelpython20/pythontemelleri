import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"OpenCV\Images\resim1.jpg",cv2.IMREAD_COLOR)

# print("Renkli",img.shape)
# print("Renkli",img[200][200])
# cv2.imshow("image",img)
# #----------------------------
# imgBW = cv2.imread(r"OpenCV\Images\resim1.jpg",cv2.IMREAD_GRAYSCALE)
# print("Siyah Beyaz",imgBW.shape)
# print("Siyah Beyaz",imgBW[200][200])
# cv2.imshow("Image Siyah Beyaz",imgBW)

px = img[100:200,100:200].copy()
img[400:500,400:500]  = px 
print(px)




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()