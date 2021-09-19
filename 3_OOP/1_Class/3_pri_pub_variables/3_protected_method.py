"""
Python's convention to make a method to be a Protected
method is to add a prefix underscore('_'). A Protected method
means, it effectively prevents it to be accessed, unless it is from
within sub-class.

In fact in python, this doesn't prevent accessing protected variables
even outside class
"""


class Car:

    def __init__(self, hour, distance):
        self.hour = hour
        self.distance = distance

    def _speed(self):
        print(self.distance/self.hour)


class Honda(Car):

    def __init__(self, hours, distance):
        super().__init__(hours, distance)

    def speed(self):
        self._speed()


honda = Honda(4, 400)
honda.speed()

# Even we can directly access it
benz = Car(6, 400)
Car._speed(benz)
