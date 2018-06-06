class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        pass

    def slope(self):
        pass


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)

print("Distance is {}".format(line.distance()))
print("Slope is {}".format(line.slope()))
