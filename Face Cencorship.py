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
        
        vidy = img[row:height+row,column:height+column] #takes detected face's coordinates to display it in a different window
        blur = cv.GaussianBlur(vidy, (51, 51), 0)  # blurring the face
        img[row:height + row, column:height+ column] = vidy


        cv.imshow("vidy.mp4", vidy) #Displaying cropped face
    cv.imshow("video.mp4",img) #full video
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
