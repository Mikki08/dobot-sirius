import cv2
import numpy as np
from serial.tools import list_ports
import pydobot



class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)


    def get_frame(self):

        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
