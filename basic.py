from libs.drone import Drone
from libs.camera import Camera
from libs.plate import Plate
import time

def main():
    drone = Drone()
    camera = Camera()

    drone.take_off()
    keep_flying = True


    plate = Plate()
    x = 0
    while x < 20:
        print x
        camera.capture()
        detected = plate.detect_plate()
        if detected:
            distance_from_center = plate.distance_from_center(camera.IMAGE_CENTER)
            drone.move(distance_from_center)
        else:
            print "noting found"
        time.sleep(1)
        x = x + 1



    time.sleep(5)

    drone.land()
    drone.disconnect()
    camera.shutdown_camera()
    time.sleep(1)

if __name__ == "__main__":
    main()
