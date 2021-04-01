import cv2 as cv
from datetime import datetime
face_cascade = cv.CascadeClassifier('resources\haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier('resources\haarcascade_eye.xml')
sideface_cascade = cv.CascadeClassifier('resources\haarcascade_profileface.xml')
cap = cv.VideoCapture(0)
cap.set(3,1080)
cap.set(4,740)
cap.set(10,100)
while True:
    success, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)
    sideface = sideface_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in sideface:
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
        cv.putText(img, 'Cheating', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
        print("Cheating...")
        now = datetime.now()
        print(now)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    for (x,y,w,h) in eyes:
        img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    for (x,y,w,h) in faces:
        img = cv.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
        cv.putText(img, 'No Cheating', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv.imshow('Face Recognition',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
