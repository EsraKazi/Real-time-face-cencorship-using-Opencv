import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    success, img = cap.read()
    img = cv.flip(img,1)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(gray,minSize=[150,150])#150,150 pixel altındaki algılanan yüzler görmezden gelinecek.Burun, yüz olarak algılandığı için eklendi

    for (column, row, width, height) in detected_faces:

        vidy = img[row:height+row,column:height+column]
        org = vidy.copy() # Algılanan yüzü göstermek için efekt eklemeden önce kopyalanıyor
        blur = cv.GaussianBlur(vidy, (51, 51), 0)  #blur atma

        height, width = blur.shape[:2]
        w, h = (8, 8) # Sansürün kaça kaç pixel olacağını belirler
        temp = cv.resize(blur, (int(w), int(h)), interpolation=cv.INTER_LINEAR) # Algılanan yüzün boyutu küçültme
        output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST) # Algılanan yüzün boyutu büyütme
        img[row:height + row, column:height+ column] = output


        cv.imshow("vidy.mp4", org)# Algılanan yüzün ayrı pencerede görüntülenmesi
    cv.imshow("video.mp4",img) #Sansür uygulanmış görüntünün tamamının görüntülenmesi
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
