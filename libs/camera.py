import picamera
import time

class Camera:

    PLATE_URL = 'plate.jpg'
    
    IMAGE_HEIGHT = 768
    IMAGE_WIDTH = 1024
    IMAGE_CENTER = {'x' : 512, 'y' : 384}

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.IMAGE_WIDTH, self.IMAGE_HEIGHT)
        time.sleep(2)
        self.camera.start_preview()

    def capture(self):
        return self.camera.capture(self.PLATE_URL)

    def shutdown_camera(self):
        self.camera.close()
