import picamera
import time

class Camera:

    PLATE_URL = 'plate.jpg'
    
    IMAGE_HEIGHT = 768
    IMAGE_WIDTH = 1024
    IMAGE_CENTER = {'x' : 512, 'y' : 384}

    def __init__():
        self.camera = picamera.PiCamara()
        self.camera.resolution = (IMAGE_WIDTH, IMAGE_HEIGHT)
        time.sleep(2)
        self.camera.start_preview()

    def capture():
        return camera.capture(PLATE_URL)

    def shutdown_camera():
        self.camera.close()