import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
yuzler_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_frontalface_default.xml")
goz_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_eye.xml")

while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler = yuzler_cascade.detectMultiScale(gri,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # gozler
        roi_gray = gri[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        gozler = goz_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



    cv2.imshow("1",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
