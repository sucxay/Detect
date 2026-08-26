import cv2 
from camera.webcam import Webcame
from detection.detector import Detector
camera= Webcame()

camera.open()
detector = Detector()
while camera.is_open():
    frame = camera.read()

    if frame is None:
        break 
    detections = detector.detect(frame)
    print("detections :")

    for detection in detections:
        print(
            detection.class_name , detection.confidence , detection.bbox
        )

    cv2.imshow("Sixth sense",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
