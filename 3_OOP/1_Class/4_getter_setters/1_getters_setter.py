"""
The main purpose of getter and setter functions is to achieve a task of Data
Encapsulation. Mainly we use them in below scenario's,

We use getter and setters to add validation logic around getting and
setting value.
To avoid direct access of a class field, so that the private variable
cannot be directly access or modified by the external user.
"""
import string
import random


class Username:
    population = string.ascii_letters + string.digits + "@$%^&[]!"

    def __init__(self):
        # It is a private variable
        self.__username = ''.join(random.sample(Username.population, k=15))

    # getting user name
    def get_username(self):
        return self.__username

    # setting username
    def set_username(self, value):
        if len(value) > 25:
            raise ValueError("Length of the username is grater than 25 letters")
        self.__username = value


user_1 = Username()
# Addition info:Accessing private variables
# print(user_1._Username__username)

# Passing value to set function
user_1.set_username("Madhu Babu Kencha")

# Getting value from set function
print(user_1.get_username())


# Passing value to set function
user_1.set_username("Madhu Babu Kenchaadsdfsadfsadfsdf")