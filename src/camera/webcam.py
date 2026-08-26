import cv2 

class Webcame:
    def __init__(self,camera_id = 0 ):
        self.camera_id = camera_id 
        self.cap= None


    def open(self):
        self.cap = cv2.VideoCapture(self.camera_id)

    def read(self):
        ret , frame = self.cap.read()

        if not ret:
            return None

        return frame

    def is_open (self):
        return self.cap is not None and self.cap.isOpened()

    def release(self):
        if self.cap is not None:
            self.cap.release()

            