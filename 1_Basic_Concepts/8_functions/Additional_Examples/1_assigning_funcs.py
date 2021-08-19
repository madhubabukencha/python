"""
In this program we will see how to assign a function to variable
After assigning both function's are different.
"""


def first(name):
    print("Hello {}".format(name))


first("James")
second = first
second("Madhu")
