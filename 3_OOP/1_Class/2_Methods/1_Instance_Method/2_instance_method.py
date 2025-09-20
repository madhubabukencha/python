"""
Name : Madhu Babu Kencha
Created : 22-Jun-2022
Last update: 20-Sep-2025
L

In this program we will learn that for instance methods
it's not possible to change class state.
"""


class Demo:
    """
    This class how to deal with class and instance variables
    and how to change them.
    """
    country = "India"

    def __init__(self):
        """
        You don't even need instance methods until and unless you
        want to deal with instance variables.
        """
        pass

    def display(self):
        print(self.country)
        # It is specific to object
        self.country = "China"

        # If you enable it, it will changes class states
        # So, that all object value changes
        # Demo.country = "China"

        print(self.country)


object_1 = Demo()
object_1.display()
object_1.country = "America"
print(object_1.country)

print("-----Creating new object-----")
# This shows that class state is not changed
object_2 = Demo()
object_2.display()

print("-----Changing class state-----")
# To change class state
Demo.country = "Russia"
object_3 = Demo()
object_3.display()
