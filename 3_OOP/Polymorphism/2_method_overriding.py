"""
The Method Overriding is a language feature that allows a subclass or child
class to provide a specific implementation of a method that is already
provided by one of its superclasses or parent classes
"""


class Honda:

    @staticmethod
    def speed(distance, time):
        print(f"Honda car speed: {distance/time}")


class Suziki(Honda):

    @staticmethod
    def speed(distance, time):
        print(f"Suziki car speed: {distance*time}")


suziki = Suziki()
suziki.speed(100, 2)