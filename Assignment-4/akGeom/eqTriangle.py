from akGeom import geom
import math as mth

class eqTriangle(geom.Geom):
    def __init__(self, side):
        self.side = side
        super().__init__()
    def area(self):
        if self.side > 0:
            return (0.5 * self.side * (self.side * mth.sqrt(3)))
        else:
            return ("Please input a positive number to calculate area.")