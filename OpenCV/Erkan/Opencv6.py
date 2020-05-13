import cv2
import numpy as np
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(1)

while True:
    ret,frame=cap.read()

    kernel=np.ones((5,5),np.float32)/25
    smooth=cv2.filter2D(frame,-1,kernel)
    blur=cv2.blur(frame,(10,10))

    cv2.imshow("Frame",frame)
    cv2.imshow("Blur",blur)
    cv2.imshow("Smooth",smooth)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()