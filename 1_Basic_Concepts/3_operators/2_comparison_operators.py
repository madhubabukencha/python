"""
Name           : Madhu Babu Kencha
created on     : 13-Sep-2018
Last Modified  : 11-Jul-2021

This program shows the usage of comparison operators
These operators also called Rational Operators
"""
a, b = 10, 15

# double equal sign(==), check whether two operands are equal or not
# If both are equal then it returns 'True' else it returns 'False'
doube_equal = (a == b)
print("10 == 15 : ", doube_equal)

# Not equal sign(!=), returns 'True' if two operands values
# are not equal and voice versa
not_equal = (a != b)
print("10 != 15 : ", not_equal)

# Less_than sign(<), returns 'True', only if right side value
# lesser than left side value, if not it returns 'False'
less_than = (a < b)
print("10 < 15 : ", less_than)

# Greater_than sign(>), returns 'True', only if right side value
# greater than the left side value. if not it returns 'False'.
greater_than= (a > b)
print("10 > 15 : ", greater_than)

# Less_than or Equal sign(<=), returns 'True' if right side
# value less than or equal to left side value
less_than_or_equal = (a <= b)
print("10 <= 15 : ", less_than_or_equal)

# Greater_than or Equal sign(<=), returns 'True' if left side
# value less then or equal to right side value(right >= left)
greater_than_or_equal = (a >= b)
print("10 >= 15 : ", greater_than_or_equal)

