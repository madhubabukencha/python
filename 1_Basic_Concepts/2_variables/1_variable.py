"""
Name           : Madhu Babu Kencha
Created on     : 06-Sep-2018
Last Modified  : 04-Jul-2021


1) In python "variables" do not need declaration to reserve memory.
2) The variable declaration or initialization happens automatically
   whenever we assign a value to a variable
3) Python is type inferred language means it will automatically detects
   the data type base on assigned value.
4) The assignment operator '=' is used to assign values to a variable

Do's
-------------------------
1) Use camelCase notation to declare a variable
2) Use Upper case letters to define constants
3) Variable names can have combination of (a-z),(A-Z),(0-9) and "_"

Don't
-------------------------
1) Don't start with digits
2) Never use special symbols like  !, @, #, $, %, etc
"""
# pylint: disable=C0103
# Defining a constant variable
PIE = 3.14
# f"" strings provide advance way of formatting.
# So, mostly I use them every where
print(f"PIE value is : {PIE}")

# Defining string variable
# Example for camelCase usage
myName_1 = "Madhu Babu"
print(f"My name is : {myName_1}")

# Defining integer variable
integer_value = 10
print(f"Integer Value :{integer_value}")

# Defining float variable
float_value = 10.9
print(f"Float value : {float_value}")

# Defining complex variable
complex_value = (4+5j)
print(f"Complex Value : {complex_value}")
