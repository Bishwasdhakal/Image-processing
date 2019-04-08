from libs.camera import Camera
from libs.plate import Plate


plate_width = 0.073

plate = Plate()
camera = Camera()
x = 0
while x < 20:
    print x
    x = x + 1

    camera.capture()
    detected = plate.detect_plate()

    if detected:
        print plate.distance_from_camara()

        pixal_width = plate.topRight['x'] - plate.bottemLeft['x']
        focal = (pixal_width * 0.5) / 0.073
        print focal