import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        # Calculate and return the area of the circle
        return round(math.pi*self.radius**2)

    def getPerimeter(self):
        # Calculate and return the perimeter (circumference) of the circle
        return round(2*math.pi*self.radius)
