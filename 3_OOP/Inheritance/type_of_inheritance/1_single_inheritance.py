"""
SINGLE INHERITANCE

Here child class gets derived from single base class.
So child class in inherits the features of single base class
"""


class Parent:
    """
    It is Base class. It will inherits it's features to
    child class
    """
    def __init__(self, name):
        self.name = name

    @staticmethod
    def mother():
        print("Parent Class: I'm a mother of this child class")

    def child_name(self):
        print(f"Parent Class: My child name is {self.name}")


class Child(Parent):
    def child(self):
        print("Child Class: I will call my mother. mummy!!!")
        # super().child_name()
        Parent.child_name(self)


object_a = Child("Madhu")
object_a.child()
object_a.mother()
