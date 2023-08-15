"""
Name   : Madhu Babu Kencha

In this program we will see how to create lambda function syntax and its usage
Functions created in this way are called anonymous

Syntax
------
lambda variableName:Expression

Returns
------
It returns a function object

Useful Links:
------------
https://realpython.com/python-lambda/
"""


def function1(func, arg):
    return func(arg)


def function2(x, y):
    return lambda z: x * y * z


if __name__ == '__main__':
    # Simple implementation of lambda
    exp = lambda x, y: x**y  # PEP 8: E731 do not assign a lambda expression, use a def
    print(F"Exponential value 2 power 4: {exp(3, 2)}")

    # Lambda function assigning to a variable
    age = lambda x: print("The Dog age is:%d" % x)
    age(10)

    # Lambda function passed as argument to other function
    print("Lambda function as argument:", function1(func=lambda x: x**2, arg=3))

    # it is equal to
    # result = function2(2, 3)
    # print(result(2))
    # >> > x = lambda z: 2 * 3 * z
    # >> > x(2)

    result = function2(2, 3)(2)
    print(result)


