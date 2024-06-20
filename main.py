import cv2
path = "/home/jvvitor307/miniconda3/envs/TrabalhoIA/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml"
clf = cv2.CascadeClassifier(path)


cap = cv2.VideoCapture(0)
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))
    cv2.imshow('frame', frame)
frame.save("/")
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)











