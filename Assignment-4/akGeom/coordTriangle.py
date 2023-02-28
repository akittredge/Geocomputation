from akGeom import geom

class coordTriangle(geom.Geom):
    def __init__(self, coordList):
        self.x1 = coordList[0][0]
        self.y1 = coordList[0][1]
        self.x2 = coordList[1][0]
        self.y2 = coordList[1][1]
        self.x3 = coordList[2][0]
        self.y3 = coordList[2][1]
        super().__init__()
    def area(self):
        return abs(0.5*(((self.x3*self.y2)-(self.x2*self.y3))-((self.x3*self.y1)-(self.x1*self.y3))+((self.x2*self.y1)-(self.x1*self.y2))))