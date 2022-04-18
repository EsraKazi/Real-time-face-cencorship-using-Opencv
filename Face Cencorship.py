import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    success, img = cap.read()
    img = cv.flip(img,1) #Flipping the camera to give mirror effect
    cv.imshow("video.mp4",img)
    if cv.waitKey(1) & 0xFF == ord('q'): #Exit when pressed q key
        break