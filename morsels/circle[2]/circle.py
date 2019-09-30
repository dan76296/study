'''Circle
This week I want you to make a class that represents a circle.
The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
For example:
c = Circle(5)
c
c.radius
c.diameter
c.area
Additionally the radius should default to 1 if no radius is specified when you create your circle
'''
import math


class Circle():

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = radius * 2
        self.area = (math.pi * radius)**2

    def __str__(self):
        return '%s(%s)' % (self, self.radius)

c = Circle(10)

print(c)
print(c.radius)
print(c.diameter)
print(c.area)