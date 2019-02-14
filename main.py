import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def display(self):
        pass
    @abc.abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.hypotlen = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    def display(self):
        print("The hypotenuse of this square is: (" \
                + str(self.x1) + "," + str(self.y1) + ") (" + str(self.x2) \
                + "," + str(self.y2) + ")")
    def area(self):
        return math.pow(self.hypotlen, 2)/2

class Circle(Shape):
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
    def display(self):
        print("This is a circle with center at point (" + str(self.x) + "," \
                + str(self.y) + "), radius " + str(self.rad))
    def area(self):
        return math.pi * 2 * self.rad

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def display(self):
        print("The three points of this triangle are: (" + str(self.x1) + "," \
                + str(self.y1) + ") (" + str(self.x2) + "," + str(self.y2) + ") (" + str(self.x3) \
                + "," + str(self.y3) + ")")
    def area(self):
        return math.abs( ( self.x1 * (self.y2 - self.y3) + self.x2 * \
            (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2) ) / 2 );
x = Circle(1, 1, 1)
y = Triangle(0, 0, 1, 0, 0, 1)
z = Square(0, 0, 1, 1)
shapes = [x, y, z]
for s in shapes:
    s.display()
