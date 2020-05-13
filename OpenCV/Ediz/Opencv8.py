import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread(r"OpenCV\Images\opencv-feature-matching-template.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread(r"OpenCV\Images\opencv-feature-matching-image.jpg",cv2.IMREAD_COLOR)

orb = cv2.ORB_create()

kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING2,crossCheck = True)

matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda x: x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:200],None,flags=2)
plt.imshow(img3)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
