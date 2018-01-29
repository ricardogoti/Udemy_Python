import cv2, time
video=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    check, frame = video.read()
    #print (check)
    #print (frame)
    #time.sleep(3)
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame,    scaleFactor=1.1,    minNeighbors=5)
    for x, y, w, h in faces:
        img=cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 3)
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key!=-1:
        break
video.release()
cv2.destroyAllWindows()
