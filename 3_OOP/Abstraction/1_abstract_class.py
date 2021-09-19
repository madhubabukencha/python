"""
1. Abstract classes are the classes that contain one or more abstract methods.
2. Abstract method is a method that is declared, but contains no implementation.
3. Abstract classes may not be instantiated, and its abstract methods must be
   implemented by its subclasses
4. Abstract method doesn't support abstraction directly, we need to import import
   Abstract Base Class(ABC) to work with abstraction

Need of Abstract Method:
Sometimes we just know the requirements but don't know how to implement.
So at that time we create abstract class. Later whatever sub classes
inherited from this abstract classes in there we provide it's implementation
"""

from abc import ABC, abstractmethod


class Car(ABC):

    # Creating abstract method
    @abstractmethod
    def speed(self):
        pass



class Suziki(Car):

    # sub-class must implement this method
    # If you don't implement you will get below error
    # TypeError: Can't instantiate abstract class Suziki with abstract methods speed
    def speed(self, hours, distance):
        print(hours * distance)
    
    def car_name(self, car):
        print(f"The speed of the {car}:")


suziki = Suziki()
suziki.car_name("Suziki")
suziki.speed(4, 150)