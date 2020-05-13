import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\Erkan ALA\Desktop\tarkan.jpg",cv2.IMREAD_COLOR)
#cap=cv2.VideoCapture(1)

goz_cascade=cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_eye.xml")
yuzler_cascade=cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_frontalface_default.xml")

#ret,frame=cap.read()
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

yuzler=yuzler_cascade.detectMultiScale(gri,1.3,5)
for (x,y,w,h)  in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gri[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    gozler=goz_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in gozler:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



cv2.imshow("1",img)
cv2.waitKey(0)
if cv2.waitKey(1)&0xFF==ord('q'):
    cv2.destroyAllWindows()



