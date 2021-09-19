"""
In this program we are going to learn how to use in built property()
method

In my view property is nothing but a smart way of using getters and setters

The property() method in python provides an interface to instance attributes.
It encapsulates instance attributes and provides a property.

The property() method takes the get, set and delete methods as arguments and
returns an object of the property class.

syntax:
property_obj = property(fget, fset, fdel, docstring)
"""


class UpdateWeather:
    def __init__(self, temperature=30):
        self._temperature = temperature

    def get_temperature(self):
        print("get method called")
        return self._temperature

    def set_temperature(self, value):
        print("Set method called")
        if type(value) != int:
            raise ValueError("Value must be an integer")
        self._temperature = value

    def del_temperature(self):
        print("Deleting object")
        del self._temperature

    property_obj = property(get_temperature, set_temperature, del_temperature)


kurnool = UpdateWeather(temperature=42)

# Getting property value
print(kurnool.property_obj)

# Setting property value
kurnool.property_obj = 50
print(kurnool.property_obj)

# Getting exception
# kurnool.property_obj = "Jasf"

# Calling delete temperature
kurnool.del_temperature()
# print(kurnool._temperature)
