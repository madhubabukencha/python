"""
A double underscore(__) prefixed to a method makes it private.
It gives a strong suggestion not to touch it from outside the
class(even in sub-class). Any attempt to do so will result
in an AttributeError

Python performs name mangling of private methods. Every member
with double underscore will be changed to _object._class__method.
If so required, it can still be accessed from outside the class,
but the practice should be refrained
"""

class Car:

    def __init__(self, hour, distance):
        self.hour = hour
        self.distance = distance

    def __speed(self):
        print(self.distance/self.hour)


class Honda(Car):

    def __init__(self, hours, distance):
        super().__init__(hours, distance)

    def speed(self):
        self.__speed()


honda = Honda(4, 400)
# Below line will cause error as private variable not accessible from
# outside class
# honda.speed()

# Even we can directly access it
benz = Car(6, 400)
benz._Car__speed()
