
import cv2

cap=cv2.VideoCapture("video/snawwfall.mp4")
while True:
    Asif,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

