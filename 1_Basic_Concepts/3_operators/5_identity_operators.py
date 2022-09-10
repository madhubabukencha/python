"""
Name           : Madhu Babu Kencha
created on     : 13-Sep-2018
Last Modified  : 11-Jul-2021

The identity operators "is" and "is not" are use to check whether
two python objects have same identity or not.

"is", will return "True" if both operands have id value is same
"is not", will return "True" if both operands have different id value
"""
x, y, z, c = 10, 11, 12, 12
print("id's of x: {}, y: {}, z: {}, c: {}".format(id(x),
                                                  id(y),  id(z), id(c)))
k = x is y
print("{} is {} : {}".format(id(x), id(y), k))
i = x is not y
print("{} is not {} : {}".format(id(x), id(y), i))
j = z is c
print("{} is {} : {}".format(id(z), id(c), j))
l = z is not c
print("{} is not {} : {}".format(id(z), id(c), l))

# Even though values are same, if they were in the list then
# then their id() value will change.
x, y = [12], [12]
k = x is y
print('{} is {} :  {} '.format(id(x), id(y), k))
