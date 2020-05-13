import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread(r"opencv-feature-matching-template.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread(r"OpenCV\Images\opencv-feature-matching-image.jpg",cv2.IMREAD_COLOR)


cv2.imshow('Corner',img)

cv2.waitKey(0)
cv2.destroyAllWindows()