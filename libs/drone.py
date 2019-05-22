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
        #self.multiranger = Multiranger(self.scf)
    

    def take_off(self, height = 1.0, velocity = 0.2):
        """has the drone take off"""
        # drone takes off
        self.motionCommander.take_off(height = height, velocity = velocity)

    def land(self):
        self.motionCommander.land()
    
    def move(self, vector):
        """moves the drone at a constant speed in one direction"""
        if vector['y'] > 0.1:
            print "move up by {}m".format(vector['y'])
            self.motionCommander.up(vector['y'], velocity=0.4)
        elif vector['y']  < -0.1:
            print "move down by {}m".format(abs(vector['y']))
            self.motionCommander.down(abs(vector['y']), velocity=0.4)
        if vector['x'] > 0.1:
            print "move left by {}m".format(vector['x'])
            self.motionCommander.left(vector['x'], velocity=0.4)
        elif vector['x'] < -0.1:
            print "move right by {}m".format(abs(vector['x']))
            self.motionCommander.right(abs(vector['x']), velocity=0.4)
        if vector['z'] > 2.1:
            print "move fowards by {}m".format(vector['z'] - 2.0)
            self.motionCommander.forward(vector['z'] - 2.0, velocity=0.4)
            self
        elif vector['z'] < 1.9:
            print "move backwards by {}m".format(2.0 - vector['z'])
            self.motionCommander.back(2.0 - vector['z'], velocity=0.4)

    def disconnect(self):
        self.scf.close_link()

    def is_close(range):
        MIN_DISTANCE = 0.4  # m

        if range is None:
            return False
        else:
            return range < MIN_DISTANCE
