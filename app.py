import cv2 as cv
import numpy as np

def empty(a):
    pass

cv.namedWindow("Scale")
cv.resizeWindow("Scale",640,250)
cv.createTrackbar("Hue Min","Scale",0,179,empty)
cv.createTrackbar("Hue Max","Scale",179,179,empty)
cv.createTrackbar("Sat Min","Scale",0,255,empty)
cv.createTrackbar("Sat Max","Scale",255,255,empty)
cv.createTrackbar("Val Min","Scale",0,255,empty)
cv.createTrackbar("Val Max","Scale",255,255,empty)

cap = cv.VideoCapture(0)
cap.set(3,380)
cap.set(4,800)
cap.set(10,100)


while True:
    success, img = cap.read()
    grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grayimg, (3,3),0)
    imgcanny = cv.Canny(blur,120,200)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min= cv.getTrackbarPos("Hue Min","Scale")
    h_max= cv.getTrackbarPos("Hue Max","Scale")
    s_min= cv.getTrackbarPos("Sat Min","Scale")
    s_max= cv.getTrackbarPos("Sat Max","Scale")
    v_min= cv.getTrackbarPos("Val Min","Scale")
    v_max= cv.getTrackbarPos("Val Max","Scale")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    uppers = np.array([h_max,s_max,v_max])  
    mask= cv.inRange(imgHSV,lower,uppers)
    imgresults = cv.bitwise_and(imgHSV,imgHSV,mask=mask)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    imgh = np.hstack([img,mask,imgresults])
    cv.imshow('Img',imgh)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()