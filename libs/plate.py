import math

class Plate:

    # focal length of piCamara
    FOCAL_LENGTH = 719.085714286

    # plate width in meters
    PLATE_WIDTH = 0.3048

    center = {'x' : 0.0, 'y' : 0.0} 

    def __init__(self, topLeft, topRight, bottemLeft, bottemRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottemLeft = bottemLeft
        self.bottemRight = bottemRight
        self.center = self.calc_center()

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

if __name__ == "__main__":
    topLeft = {'x' : 0, 'y' : 1000}
    topRight = {'x' : 1000, 'y' : 1000}
    bottemLeft = {'x' : 0, 'y' : 0}
    bottemRight = {'x' : 1000, 'y' : 0}
    plate = Plate(topLeft, topRight, bottemLeft, bottemRight)
    print plate.calcCenter()