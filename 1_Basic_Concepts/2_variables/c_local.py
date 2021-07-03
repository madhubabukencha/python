"""
Name           : Madhu Babu Kencha
Created on     : 06-Sep-2018
Last Modified  : 07-Jul-2021

local variable
--------------
Local variables are defined inside a function or in the local scope
These functions access only limited upto that function
"""


def main():
    """
    Function which demonstrate the usage of local variable
    """
    # Defining local variable
    name = "madhu"
    print("From function : ", name)


if __name__ == '__main__':
    main()
    # Accessing a local variable from outside cause an error
    # NameError: name 'name' is not defined
    # print("Outside function", name)
