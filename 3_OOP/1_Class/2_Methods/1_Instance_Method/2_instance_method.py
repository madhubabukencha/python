"""
Name : Madhu Babu Kencha
Date : 22-Jun-2022

In this program we will learn that for instance methods
it's not possible to change class state.
"""


class Demo:
    country = "India"

    def __init__(self):
        pass

    def display(self):
        print(self.country)
        # It is specific to object
        self.country = "Chain"
        # If you enable it, it will changes class states
        # So, that all object value changes
        # Demo.country = "China"
        print(self.country)


object_1 = Demo()
object_1.display()
object_1.country = "America"
print(object_1.country)
print("\n")
object_2 = Demo()
object_2.display()
print("\n")
object_3 = Demo()
object_3.display()
