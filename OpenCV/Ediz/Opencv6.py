import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
tempimg = cv2.imread(r"OpenCV\Images\temp.jpg",0)
while True:
    ret,frame = cap.read()

    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    w,h = tempimg.shape[::-1]


    res = cv2.matchTemplate(gri,tempimg,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    
    cv2.imshow("1",frame)


    # kernel = np.ones((5,5),np.float32)/25
    # smooth = cv2.filter2D(frame,-1,kernel)
    # blur = cv2.blur(frame,(10,10))


    # cv2.imshow("Frame",frame)
    # cv2.imshow("Blur",blur)
    # cv2.imshow("Smooth",smooth)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
