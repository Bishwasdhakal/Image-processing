import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

from direction import Direction

class Drone:
    """Drone instance. Starts and flies drone"""
    logging.basicConfig(level=logging.ERROR)

    def __init__(self, URI):
    """
    Init commad connects to drone
    :param URI: URI
    """
        self._cf = Crazyflie(rw_cache='./cache')
        cflib.crtp.init_drivers(enable_debug_driver=False)
        scf = SyncCrazyflie(URI, cf = self._cf)
        self.motionCommander = MotionCommander(scf)
        self.multiranger = Multiranger(scf)
    

    def start_drone(height = 0.3, velocity = 0.2):
    """has the drone take off"""
        # drone takes off
        self.motionCommander.take_off(height = height, velocity = velocity)

    def land_drone(self):
        self.motionCommander.land()
    
    def move(direction, vector):
    """moves the drone at a constant speed in one direction"""
        if direction is Direction.UP:
            print "move up"
        elif direction is Direction.DOWN:
            print "move down"
        elif direction is Direction.LEFT:
            print "move left"
        elif direction is Direction.RIGHT:
            print "move right"
        elif direction is Direction.FOWARDS:
            print "move fowards"
        elif direction is Direction.BACKWARDS:
            print "move backwards"
        else:
            print "Invalid command"


    def is_close(range):
        MIN_DISTANCE = 0.4  # m

        if range is None:
            return False
        else:
            return range < MIN_DISTANCE
