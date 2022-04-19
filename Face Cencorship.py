import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    success, img = cap.read()
    img = cv.flip(img,1)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray)

    for (column, row, width, height) in detected_faces:
        vidy = cv.rectangle(img,(column,row), (column+height, row+width),(0,0,255), 5)# Drawing a red box around the face to show detected face
        
    cv.imshow("video.mp4",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
