from picamera import PiCamera
from time import sleep
import datetime
camera = PiCamera()
while(True):
    timestamp = datetime.now()
    camera.capture('images/image{timestamp}.jpg')
    sleep(10)