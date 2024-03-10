"""
Name: Madhu Babu Kencha

This program will show you how to construct a function with
parameters.
Mandatory Read: different_kinds_of_args.md
"""


def function1(x, y, z):
    """
    This function takes 3 parameters. These required parameters, if
    you don’t value then this function will through an TypeError error.
    """
    print("function1 values:", x, y, z)


def function2(a, b=0, c=1):
    print("function2 values:", a, b, c)


def function_3(a, *, b, c, d=4):
    """
    '*' makes you mandatory to pass keys(b, c, d) at time of function calls
    """
    print(f"{a=}, {b=}, {c=}, {d=}")


if __name__ == "__main__":
    function1(2, 3, 4)
    # Passing less input than required causes an error
    # function1(1,2)

    function2(5)
    function2(7, 8, c=20)
    function2(c=1, b=6, a=3)  # Order is not mandatory if you pass keywords
    # Calling function in below format throws an error
    # SyntaxError: positional argument follows keyword argument
    # function2(c=1, b=6, 3)
    # function2(44, b=4, 34)

    function_3(10, b=5, c=4, d=7)


