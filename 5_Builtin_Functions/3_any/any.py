"""
The any function returns true if any element iterable is true.
all elements are true                        --> True
one element is true and rest all false       --> True

syntax: any(iterable)

NOTE:
0               --> Represents the False
any empty thing --> Represents the False
1 or any number --> Represents the True
'any string'    --> Represents the True
"""

# IN CASE OF LIST AND TUPLE
print("IN CASE OF LIST AND TUPLE:")
n = [True, True, True]
print(any(n))
m = (True, False, False)
print(any(m))
o = (False, False, False)
print(any(o))
p = (-1, 2, 23)
print(any(p))
q = (0, 0, 0)
print(any(q))
r = []
print(any(r))


# IN-CASE OF STRINGS
print("\nIN-CASE OF STRINGS:")
print(any(""))
# Space also considered as a string but not as an empty string
print(any(" "))
print(any("name"))


# IN-CASE OF DICTIONARY
# In case of dictionary if all are keys(not values) False then only it will return False
print("\nIN-CASE OF DICTIONARY:")
x = {1: 1, 2: '2'}
print(any(x))
print(any({0: 1, False: 2}))
print(any({'0': 2, False: 4}))
