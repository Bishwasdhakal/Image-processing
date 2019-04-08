import math

class Plate:
    PLATE_URL = 'plate.jpg'

    # focal length of piCamara
    FOCAL_LENGTH = 719.085714286

    # plate width in meters
    PLATE_WIDTH = 0.3048

    center = {'x' : 0.0, 'y' : 0.0} 

    def calc_center(self):
        self.center['x'] = (self.topLeft['x'] + self.bottemRight['x']) / 2.0
        self.center['y'] = (self.topLeft['y'] + self.bottemRight['y']) / 2.0
        return self.center

    def distance_from_center(img_center):
        """
        :param img_center = the center of the image
        :returns a vector of distance and directio
        """
        return {"x" : img_center.x - self.center.x, "y" : img_center.y - self.center.y}

    def distance_from_camara(self):
        """
        :Plate plate the license plate
        returns the estimated distance of the plate to the drone 
        """
        pixalWidth = self.topRight.x - self.topLeft.x
        
        distance = (FOCAL_LENGTH / PLATE_WIDTH) * pixalWidth
        return distance

    def horizontal_angle(self):
        """measures how scewed the plate is in terms of the camara"""
        hypotenuse = math.sqrt(
            (self.topLeft.x - self.topRight.x)^2 + 
            (self.topLeft.y - self.topRight.y)^2)
        opposite = self.topRight.x - self.topLeft.x

        angle = math.asin(opposite / hypotenuse)
        return math.degrees(angle)

    def detect_plate():
        """
        looks for a plate in the image and then returns the center of the plate coordinates
        """
        bashCommand = 'alpr -j -n 1 ' + PLATE_URL
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
                self.topLeft = {'x' :plateObject.results[0].coordinates[0].x, 'y' :plateObject.results[0].coordinates[0].y}
                self.topRight = {'x' :plateObject.results[0].coordinates[1].x, 'y' :plateObject.results[0].coordinates[1].y}
                self.bottemLeft = {'x' :plateObject.results[0].coordinates[3].x, 'y' :plateObject.results[0].coordinates[3].y}
                self.bottemRight = {'x' :plateObject.results[0].coordinates[2].x, 'y' :plateObject.results[0].coordinates[2].y}