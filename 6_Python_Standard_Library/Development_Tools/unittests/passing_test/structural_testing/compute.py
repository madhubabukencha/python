"""
Date : 29-06-2019

In this program we are simply going to create a function
which returns the full_names
"""


def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def addition(x, y):
    return x+y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return x/y
