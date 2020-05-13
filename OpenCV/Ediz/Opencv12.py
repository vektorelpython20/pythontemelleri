import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
yuzler_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_frontalface_default.xml")
goz_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_eye.xml")
img = cv2.imread(r"OpenCV\Images\yuz2.PNG")
gozluk = cv2.imread(r"OpenCV\Images\sunglasses.png")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
merkez = []
yuzler = yuzler_cascade.detectMultiScale(gri,1.3,5)
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gri[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    gozler = goz_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in gozler:
        merkez.append((x+int(ex + 0.5*ew),y+int(ey+0.5*eh)))

    if len(merkez) > 0:
        gozluk_w = 2.12 * abs(merkez[1][0]-merkez[0][0])
        overimg = np.ones(img.shape,np.uint8) * 255
        h,w = gozluk.shape[:2]
        buyume_faktor = gozluk_w/w
        overgozluk = cv2.resize(gozluk,None,fx=buyume_faktor,fy=buyume_faktor,interpolation=cv2.INTER_AREA)
        x  = merkez[0][0] if merkez[0][0] < merkez[1][0] else merkez[1][0]
        x -= 0.26*overgozluk.shape[1]
        y += 0.35*overgozluk.shape[0]

        h,w = overgozluk.shape[:2]

        overimg[int(y):int(y+h),int(x):int(x+w)]=overgozluk

        grigozluk = cv2.cvtColor(overimg,cv2.COLOR_BGR2GRAY)

        ret,mask = cv2.threshold(grigozluk,110,255,cv2.THRESH_BINARY)

        mask_inv = cv2.bitwise_not(mask)

        temp = cv2.bitwise_and(img,img,mask=mask)
        temp2 = cv2.bitwise_and(overimg,overimg,mask=mask_inv)

        son = cv2.add(temp,temp2)

        cv2.imshow("deneme",son)


cv2.waitKey(0)

cv2.destroyAllWindows()
