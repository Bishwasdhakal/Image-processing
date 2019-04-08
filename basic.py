from libs.drone import Drone
from libs.camera import Camera
import time

def main():
    drone = Drone()
    camera = Camera()

    drone.take_off()
    time.sleep(5)

    drone.land()
    drone.disconnect()
    camera.shutdown_camera()

if __name__ == "__main__":
    main()