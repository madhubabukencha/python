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


# Lambda function passed as a argument to other function
def function1(func, arg):
    return func(arg)


def function2(x, y):
    return lambda z: x * y * z


if __name__ == '__main__':
    print("Lambda function as argument:", function1(lambda x: x**2, 3))

    # it is equal to
    # result = function2(2, 3)
    # print(result(2))
    result = function2(2, 3)(2)
    print(result)

    # Lambda function assigning to a variable
    age = lambda x: print("The Dog age is:%d" % x)
    age(10)

