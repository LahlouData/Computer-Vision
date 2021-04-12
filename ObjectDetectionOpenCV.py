import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("ressources/haarcascade_frontalface_default.xml")
faceCascade1 = cv2.CascadeClassifier("ressources/haarcascade_eye.xml")
#faceCascade2 = cv2.CascadeClassifier("ressources/haarcascade_smile.xml")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    succes, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imgGray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    faces1 = faceCascade1.detectMultiScale(imgGray1, 1.1,4)
    #faces2 = faceCascade2.detectMultiScale(imgGray1, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Head", (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 1)

    for (a, b, c, d) in faces1:
        cv2.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 2)
        cv2.putText(img, "eye", (a, b), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 1)
    #for (z, e, r, t) in faces2:
     #   cv2.rectangle(img, (z, e), (z + r, e + t), (255, 0, 0), 2)

    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break