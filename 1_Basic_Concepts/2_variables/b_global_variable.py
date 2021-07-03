"""
Name           : Madhu Babu Kencha
Created on     : 06-Sep-2018
Last Modified  : 07-Jul-2021

global variables
----------------
Global variables we can access throughout the program
Usually we define all global variables at the top of
of file.

NOTE :
If you try to modify a global variable value inside a
function then it through "UnboundLocalError" exception.

To avoid that exception either create same variable
locally(I mean in function,etc ..,) or define a variable
with "global"
eg:
variable_name = variable_value
def function():
    global variable_name
    return variable_name
"""

# Defining global variable
x = 4


def main():
    """
    Function which demonstrate the usage of global variable
    """
    # Commenting of "global x" throws an below error
    # UnboundLocalError: local variable 'x' referenced before assignment
    global x
    # To void errors we need to reference variable locally like below
    # x = 3
    x = x*2
    print("From function : ", x)


if __name__ == '__main__':
    # see the difference in the output by uncommenting below line
    # main()
    print("global variable value : ", x)
    main()
