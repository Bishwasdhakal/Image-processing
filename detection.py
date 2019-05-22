from libs.camera import Camera
from libs.plate import Plate
import time

def main():
    camera = Camera()
    print 'Camera is ready'

    plate = Plate()
    status = True
    x = 0
    while x < 10:
        print x
        x = x + 1
        camera.capture()
        print 'image captured'
        plate_detected = plate.detect_plate()
        time.sleep(1)
        if plate_detected:
            print 'Found!!!!!'
            distance_from_center = plate.distance_from_center(camera.IMAGE_CENTER)
                #drone.move(distance_from_center)
            move(distance_from_center)
        print "move! back!! you have two seconds!!!!"
        time.sleep(2)
def move(vector):
    """moves the drone at a constant speed in one direction"""
    if vector['y'] > 0:
        print "move up by {0} meters".format(vector['y'])
        #self.motionCommander.up(vector['y'])
    elif vector['y']  < 0:
        print "move down by {0} meters".format(abs(vector['y']))
        #self.motionCommander.down(abs(vector['y']))
    if vector['x'] > 0:
        print "move left by {0} meters".format(vector['x'])
        #self.motionCommander.left(vector['x'])
    elif vector['x'] < 0:
        print "move right by {0} meters".format(abs(vector['x']))
        #self.motionCommander.right(abs(vector['x']))
    if vector['z'] > 1:
        print "move fowards by {0} meters".format(vector['z'] - 1)
        #self.motionCommander.forward(vector['z'] - 1)
    elif vector['z'] < 1:
        print "move backwards by {0} meters".format(1 - vector['z'])
        #self.motionCommander.back(1 - vector['z'])
    else:
        print "Invalid command"

if __name__ == "__main__":
    main()
