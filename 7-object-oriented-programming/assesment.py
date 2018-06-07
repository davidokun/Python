import math

print("# CLASS LINE\n")


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # Tuple unpacking
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slope(self):
        # Tuple unpacking
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)

print("Distance between {} and {} is {}".format(coordinate1, coordinate2, line.distance()))
print("Slope between {} and {} is {}".format(coordinate1, coordinate2, line.slope()))

print("# CLASS CYLINDER\n")


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius**2) * self.height

    def surface_area(self):
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius**2)


cylinder = Cylinder(2, 3)

print("Volume is {v:1.3f}".format(v=cylinder.volume()))
print("Total Surface Area is {s:.3f}".format(s=cylinder.surface_area()))

