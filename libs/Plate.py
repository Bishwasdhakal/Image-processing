class Plate:
    center = {'x' : 0.0, 'y' : 0.0} 

    def __init__(self, topLeft, topRight, bottemLeft, bottemRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottemLeft = bottemLeft
        self.bottemRight = bottemRight

    def calcCenter(self):
        self.center['x'] = (self.topLeft['x'] + self.bottemRight['x']) / 2.0
        self.center['y'] = (self.topLeft['y'] + self.bottemRight['y']) / 2.0
        return self.center
    
if __name__ == "__main__":
    topLeft = {'x' : 0, 'y' : 1000}
    topRight = {'x' : 1000, 'y' : 1000}
    bottemLeft = {'x' : 0, 'y' : 0}
    bottemRight = {'x' : 1000, 'y' : 0}
    plate = Plate(topLeft, topRight, bottemLeft, bottemRight)
    print plate.calcCenter()