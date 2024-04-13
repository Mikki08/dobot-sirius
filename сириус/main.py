#from camera import Camera
from flask import Flask, render_template, Response
import cv2
class Camera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)

  def get_frame(self):
    ret, frame = self.video.read()
    frame = cv2.resize(frame, (480, 360))  # Resize the frame to 480x360
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

app = Flask('Test')

@app.route('/')
def index():
  return Response(gen(Camera()),
                 mimetype='multipart/x-mixed-replace; boundary=frame')
  #eturn render_template('index.html')

def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen(Camera()),
  mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='10.10.201.127', port =8000, debug=False, threaded=False)