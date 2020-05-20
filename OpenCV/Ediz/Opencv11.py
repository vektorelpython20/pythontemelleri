import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
yuzler_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_frontalface_default.xml")
goz_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_eye.xml")
gozluk = cv2.imread(r"OpenCV\Images\sunglasses.png")


while True:
    # cv2.imshow("1",gozluk)
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    vh,vw = frame.shape[:2]
    vh,vw = int(vh),int(vw)

    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    merkez = []
    yuzler = yuzler_cascade.detectMultiScale(gri,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # gozler
        roi_gray = gri[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        gozler = goz_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in gozler:
            merkez.append((x + int(ex + 0.5*ew), y + int(ey + 0.5*eh)))

        if len(merkez) > 0:
            h,w = gozluk.shape[:2]
            goz_uzaklik = abs(merkez[1][0] - merkez[0][0])
            gozlukw = 2.12 * goz_uzaklik
            buyume_faktor = gozlukw/w
            overgozluk = cv2.resize(gozluk,None,fx=buyume_faktor,fy=buyume_faktor,interpolation=cv2.INTER_AREA)
            x  = merkez[0][0] if merkez[0][0] < merkez[1][0] else merkez[1][0]
            x -= int(0.26*overgozluk.shape[1])
            y += int(0.26*overgozluk.shape[0])
            h,w = overgozluk.shape[:2]
            h, w = int(h), int(w)

            roi = frame[y:y+h, x:x+w]

            gray_over_gozluk = cv2.cvtColor(overgozluk, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_over_gozluk, 180, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)

            try:
                # Use the mask to extract the face mask region of interest 
                maskeli_yuz = cv2.bitwise_and(overgozluk, overgozluk, mask=mask) 
                # Use the inverse mask to get the remaining part of the image 
                maskeli_frame = cv2.bitwise_and(roi, roi, mask=mask_inv) 
            except cv2.error as e:
                print('aritmetik hata: '+ str(e))
                #raise e  
            frame[y:y+h, x:x+w] = cv2.add(maskeli_yuz, maskeli_frame)  
    else:
        print('Göz tespit edilemedi')    



    cv2.imshow("1",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
