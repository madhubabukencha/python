"""
Author      : Madhu Babu Kencha
Created on  : 22-09-2018

1) Inheritance provides a way to access already existing class
   without modifying any thing
2) The newly formed class is called derived class or child class
3) The existing class called base class or parent class
"""


# Defining a base class
class Vehicle:

    def __init__(self):
        print("Below are the car details")

    def name(self):
        print("Car name is Benz")

    def working_status(self):
        print("Very very good")


# Defining child class
class Nano(Vehicle):

    def __init__(self):
        # The super method is used to access parent class methods
        super().__init__()
        print("Car name is Nano")

    def cost(self):
        print("Car cost is RS 200000")

    def working_status(self):
        print("Working condition is poor")

    def speed(self, hours, distance):
        print(hours * distance)


car_details = Nano()
car_details.cost()
car_details.working_status()
