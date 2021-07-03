"""
Name           : Madhu Babu Kencha
Created on     : 06-Sep-2018
Last Modified  : 07-Jul-2021

nonlocal variables
------------------
Non local variables are used in nested functions
whose local scope is not defined. Which means the
variable can neither in the local scope nor in the
global scope
"""
# pylint: disable= C0103, W0621

variable = "global"


def outer():
    """
    This function shows how outer function value changed due to inner function
    """
    # To use nonlocal variable you must define local variable
    # or you get below error
    # SyntaxError: no binding for nonlocal 'variable' found
    variable = "local"

    def inner():
        # Defining nonlocal variable
        # Comment below line and see difference
        nonlocal variable
        variable = "non local"
        print("Inner value : ", variable)
    inner()
    print("Outer value : ", variable)


if __name__ == '__main__':
    outer()
    print("Global value : ", variable)
