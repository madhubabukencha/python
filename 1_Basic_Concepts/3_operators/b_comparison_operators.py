"""
Name           : Madhu Babu Kencha
created on     : 13-Sep-2018
Last Modified  : 05-Jul-2021

This program shows the usage of comparison operators
These operators also called Rational Operators
"""
a, b = 10, 15

# Equal sign(==), check whether two operands are equal or not
# If it both are equal it returns 'true' else it return 'false'
equal_sign = (a == b)
print("10 == 15 : ", equal_sign)

# Not equal sign(!=), returns 'true' if two operand values
# are not equal and voice versa
not_equal_sign = (a != b)
print("10 != 15 : ", not_equal_sign)

# Less_than sign(<), returns 'True' if right side value
# lesser than left side value
less_than_sign = (a < b)
print("10 < 15 : ", less_than_sign)

# Greater_than sign(>), returns 'True' if left side value
# lesser than left side value
greater_than_sign = (a > b)
print("10 > 15 : ", greater_than_sign)

# Less_than or Equal sign(<=), returns 'True' if right side
# value less than or equal to left side value
less_than_or_equal = (a <= b)
print("10 <= 15 : ", less_than_or_equal)

# Greater_than or Equal sign(<=), returns 'True' if left side
# value less then or equal to right side value(right > left)
greater_than_or_equal = (a >= b)
print("10 >= 15 : ", greater_than_or_equal)

# "is", will return True if both operand id value is same, else return False
# "is not", will return True if both operand id value is different,
# else return False
x, y, z, c = 10, 11, 12, 12
print(id(x), id(y),  id(z), id(c))
k = x is y
print("{} is {} : {}".format(id(x), id(y), k))
i = x is not y
print("{} is not {} : {}".format(id(x), id(y), i))
j = z is c
print("{} is {} : {}".format(id(z), id(c), j))
l = z is not c
print("{} is not {} : {}".format(id(z), id(c), l))

# ID value changes if it in the list, even for same value
x, y = [12], [12]
k = x is y
print('{} is {} :  {} '.format(id(x), id(y), k))  # it's id value is different
