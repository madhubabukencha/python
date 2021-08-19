"""
Higher Order Function:
Higher Order Function is function which takes a function as
an argument and return a function as output
"""


def increment(value):
    return value+1


def decrement(value):
    return value-1


def operate(function, x):
    result = function(x)
    return result


if __name__ == "__main__":
    print(operate(increment, 3))
    print(operate(decrement, 3))
