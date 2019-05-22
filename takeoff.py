from libs.drone import Drone
import time

drone = Drone(URI='radio://0/80/2M')
#drone = Drone()

drone.take_off()
time.sleep(5)
drone.land()
drone.disconnect()

