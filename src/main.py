import cv2 
from camera.webcam import Webcame

camera= Webcame()

camera.open()

while camera.is_open():
    frame = camera.read()

    if frame is None:
        break 
    cv2.imshow('demo cam' , frame)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
