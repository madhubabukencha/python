"""
In this program we are going to use property decorator instead
of property method. The property decorator and method functionality
same
"""


class UpdateWeather:
    def __init__(self, temperature=30):
        self._temperature = temperature

    @property
    def get_temperature(self):
        print("get method called")
        return self._temperature

    # Name should be same as getter method
    @get_temperature.setter
    def set_temperature(self, value):
        print("Set method called")
        if type(value) != int:
            raise ValueError("Value should be integer")
        self._temperature = value

    @get_temperature.deleter
    def del_temperature(self):
        print("Deleting object")
        del self._temperature


kurnool = UpdateWeather(temperature=42)

# Getting Value
print(kurnool.get_temperature)

# Setting value
kurnool.set_temperature = 50
print(kurnool.get_temperature)

# Deleting value
del kurnool.del_temperature
# print(kurnool._temperature)
