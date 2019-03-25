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

    """
    Init commad connects to drone
    default height is 0.3m
    default take-off velocity is 0.2
    """
    def __init__(self, URI, height = 0.3, velocity = 0.2):
        self.height = height
        self.velocity = velocity
        self._cf = Crazyflie(rw_cache='./cache')
        cflib.crtp.init_drivers(enable_debug_driver=False)
        scf = SyncCrazyflie(URI, cf = self._cf)
        self.motionCommander = MotionCommander(scf)
        self.multiranger = Multiranger(scf)
    

    def start_drone():
    """has the drone take off"""
        # drone takes off
        self.motionCommander.take_off(height=self.height, velocity=self.velocity)


    
    def move(direction):
    """moves the drone at a constant speed in one direction"""
        if direction is Direction.UP:
            print "move up"
        if direction is Direction.DOWN:
            print "move down"
        if direction is Direction.LEFT:
            print "move left"
        if direction is Direction.RIGHT:
            print "move right"
        if direction is Direction.FOWARDS:
            print "move fowards"
        if direction is Direction.BACKWARDS:
            print "move backwards"
        else:
            print "Invalid command"


    def is_close(range):
        MIN_DISTANCE = 0.4  # m

        if range is None:
            return False
        else:
            return range < MIN_DISTANCE
