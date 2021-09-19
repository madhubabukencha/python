"""
Name: Madhu Babu Kencha
Date: 04-07-2021

In this program we can see how to apply class decorator
"""
from datetime import datetime


class CalculateAge:
    """
    This class helps in demonstrating class methods by building
    age calculator
    """

    # Inplace of cls, class object will come
    @classmethod
    def your_age(cls, old_date, name):
        current_date = datetime.now()
        print(f"{name} your age is {current_date.year - old_date.year}")


# Creating class method
olddate = datetime(1996, 5, 13, 11, 30, 4)
CalculateAge.your_age(olddate, "Madhu Babu Kencha")

# You can also create call using an object
jack_sparrow = CalculateAge()
olddate = datetime(2000, 5, 14, 11, 30, 4)
jack_sparrow.your_age(olddate, "Jack Sparrow")
