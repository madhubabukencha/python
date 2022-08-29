"""
Name : Madhu Babu Kencha
Data : 22-Jun-2022

A static method does not receive an implicit first argument.
A static method is also a method that is bound to the class
and not the object of the class. This method can’t access
or modify the class state. It is present in a class because
it makes sense for the method to be present in class.
"""


class Demo:
    nationality = "Indian"

    def display():
        # static methods does not have access to class properties
        # print(nationality)
        print("Welcome to static method")


Demo.display = staticmethod(Demo.display)
print(type(Demo.display))
Demo.display()
