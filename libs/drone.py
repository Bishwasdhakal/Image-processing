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

    URI = 'radio://0/80/250K'

    def __init__(self, URI='radio://0/80/250K'):
        """
        Init commad connects to drone
        :param URI: URI
        """
        self._cf = Crazyflie(rw_cache='./cache')
        cflib.crtp.init_drivers(enable_debug_driver=False)
        self.scf = SyncCrazyflie(URI, cf = self._cf)
        self.scf.__enter__()
        self.motionCommander = MotionCommander(self.scf)
        self.multiranger = Multiranger(self.scf)
    

    def take_off(self, height = 0.3, velocity = 0.2):
        """has the drone take off"""
        # drone takes off
        self.motionCommander.take_off(height = height, velocity = velocity)

    def land(self):
        self.motionCommander.land()
    
    def move(self, vector):
        """moves the drone at a constant speed in one direction"""
        if vector['y'] > 0:
            print "move up"
            self.motionCommander.up(vector['y'])
        elif vector['y']  < 0:
            print "move down"
            self.motionCommander.down(abs(vector['y']))
        if vector['x'] > 0:
            print "move left"
            self.motionCommander.left(vector['x'])
        elif vector['x'] < 0:
            print "move right"
            self.motionCommander.right(abs(vector['x']))
        if vector['z'] > 1:
            print "move fowards"
            self.motionCommander.forward(vector['z'] - 1)
            self
        elif vector['z'] < 1:
            print "move backwards"
            self.motionCommander.back(1 - vector['z'])
        else:
            print "Invalid command"

    def disconnect(self):
        self.scf.close_link()

    def is_close(range):
        MIN_DISTANCE = 0.4  # m

        if range is None:
            return False
        else:
            return range < MIN_DISTANCE
