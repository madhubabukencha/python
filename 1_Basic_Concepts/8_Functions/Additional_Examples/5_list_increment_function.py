"""
This function shows how a list increments as per it's call.
"""


def my_list(a, increment_list=[]):
    increment_list.append(a)
    return increment_list


print(my_list(1))
print(my_list(2))
print(my_list(3))
