"""
This basic class will calculate the area and perimeter of the circle.
The purpose of this class is to understand how test cases works with classes
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
