"""
Name     : Madhu Babu Kencha

In this program we are going to see difference
between "print" and "return" in functions
"""


def function1():
    """
    This function prints the value to the console whenever it was called.
    If you call this function inside print functions, as the data
    already printed in this function, the print function returns none.
    """
    print("Hi, welcome")


def function2():
    """
    This function returns a value and terminate the function.
    """
    k = "Madhu"
    return k


if __name__ == '__main__':
    print(function1)
    print(function1())

    print(function2)
    print(function2())
