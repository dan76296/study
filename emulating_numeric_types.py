from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # get the string representation of the object so it isn't just displayed as <vector object at 0x10230110>
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other): 
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)  # this is useful, to loop back to __init__

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
