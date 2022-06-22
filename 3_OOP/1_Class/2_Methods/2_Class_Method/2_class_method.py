"""
Name: Madhu Babu Kencha
Date: 04-07-2021

In this program we can see how to apply class decorator

It can modify a class state that would apply across all the
instances of the class. For example, it can modify a class
variable that will be applicable to all the instances.
"""
from datetime import datetime


class CalculateAge:
    """
    This class helps in demonstrating class methods by building
    age calculator
    """
    birth_place = "India"

    def __init__(self, interests):
        self.interest = interests

    def display(self):
        print(self.birth_place)

    # Inplace of cls, class object will come
    @classmethod
    def your_age(cls, old_date, name):
        # It changes class state that would apply across all the
        # instances of the class
        cls.birth_place = "Pakistan"
        current_date = datetime.now()
        print(f"{name} your age is {current_date.year - old_date.year}")


# Creating class method
olddate = datetime(1996, 5, 13, 11, 30, 4)
print(CalculateAge.birth_place)
CalculateAge.your_age(olddate, "Madhu Babu Kencha")
print(CalculateAge.birth_place)

# You can also create call using an object
jack_sparrow = CalculateAge("Playing chess")
olddate = datetime(2000, 5, 14, 11, 30, 4)
print(jack_sparrow.birth_place)

