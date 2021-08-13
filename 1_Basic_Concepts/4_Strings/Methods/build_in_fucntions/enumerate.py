"""
Date  : 09-06-2019

The enumerate() function returns the enumerate object.
It contains the index and value of all the characters
in the string as pair
"""

message = "Welcome to Python"
enum_object = enumerate(message)
for number, word in enum_object:
    print("{0:<3} : {1}".format(number, word))
