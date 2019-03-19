import json
import subprocess
import time
import picamera
from collections import namedtuple
from libs.Plate import Plate

plateUrl = 'plate.jpg'

def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        imageCenter = {'x' : 512, 'y' : 384}
        # Camera warm-up time
        time.sleep(2)
        camera.start_preview()
        print "camara ready!"
        while True:
            camera.capture("plate.jpg")
            plateCenter = plateDetection()
            
            time.sleep(1)

def plateDetection():
    """
    looks for a plate in the image and then returns the center of the plate coordinates
    """
    bashCommand = 'alpr -j -n 1 ' + plateUrl
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error is not None:
        print error
    else:
        #print output
        plateObject = json.loads(str(output), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        if len(plateObject.results) <= 0:
            print "no plate detected"
        else:
            print plateObject
            print "plate is: " + str(plateObject.results[0].plate)
            print "image height: " + str(plateObject.img_height)
            topLeft = {'x' :plateObject.results[0].coordinates[0].x, 'y' :plateObject.results[0].coordinates[0].y}
            topRight = {'x' :plateObject.results[0].coordinates[1].x, 'y' :plateObject.results[0].coordinates[1].y}
            bottemLeft = {'x' :plateObject.results[0].coordinates[3].x, 'y' :plateObject.results[0].coordinates[3].y}
            bottemRight = {'x' :plateObject.results[0].coordinates[2].x, 'y' :plateObject.results[0].coordinates[2].y}

            plate = Plate(topLeft, topRight, bottemLeft, bottemRight)
            center = plate.calcCenter()
            print center
            return plate

def centerDrone(centerCoordinates, plateCenter):
    print "centering"

if __name__ == "__main__":
    main()
