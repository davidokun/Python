import math

print("# CLASS LINE\n")


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)

print("Distance between {} and {} is {}".format(coordinate1, coordinate2, line.distance()))
print("Slope between {} and {} is {}".format(coordinate1, coordinate2, line.slope()))

print("# CLASS CYLINDER\n")


class Cylinder:

    def __init__(self, height=1, radius=1):
        pass

    def volume(self):
        pass

    def surface_area(self):
        pass


cylinder = Cylinder(2, 3)

print(cylinder.volume())
print(cylinder.surface_area())

