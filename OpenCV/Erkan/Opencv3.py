import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"OpenCV\Images\resim1.jpg",cv2.IMREAD_COLOR)


cv2.line(img,(50,50),(150,150),(255,255,255),5)
cv2.rectangle(img,(50,50),(150,150),(255,0,0),5)
cv2.circle(img,(100,100),50,(0,255,0),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"Python20 Erkan",(50,50),font,1,(255,255,255),2,cv2.LINE_AA)




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()