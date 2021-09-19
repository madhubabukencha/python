"""
Name   :Madhu Babu Kencha
Date   : 03-may-2020

In this program we are going to see how to use classmethod()

Use of classmethod():
classmethod() function is used in factory design patterns
where we want to call many functions with the class name
rather than object.

Good Resources:
https://www.programiz.com/python-programming/methods/built-in/classmethod
https://www.geeksforgeeks.org/classmethod-in-python/
"""
from datetime import datetime


class CalculateAge:
    """
    This class helps in demonstrating class methods by building
    age calculator
    """
    
    # Inplace of cls, class object will come
    def your_age(cls, old_date, name):
        current_date = datetime.now()
        print(f"{name} your age is {current_date.year-old_date.year}")

  
# Creating class method
CalculateAge.your_age = classmethod(CalculateAge.your_age)
print(CalculateAge.your_age)
olddate = datetime(1996, 5, 13, 11, 30, 4)
CalculateAge.your_age(olddate, "Madhu Babu Kencha")





