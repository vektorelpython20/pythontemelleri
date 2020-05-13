import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(1)
fgbg =  cv2.createBackgroundSubtractorMOG2()

while 1:
    ret,frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow("Maske",fgmask)
    cv2.imshow("Normal",frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
