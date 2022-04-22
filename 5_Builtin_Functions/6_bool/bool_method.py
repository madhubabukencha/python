"""
Date: 22-04-2022

The bool() method analyze the data you passed in as argument
using standard truth testing procedure and returns either
True or False

We can use boolean method to check the data we are receiving
is empty or it's length equal to zero. If it is then it will
return False

standard testing procedure:
https://docs.python.org/3/library/stdtypes.html#truth
"""

# STRING TYPE
print(bool(""))
print(bool("Jokes"), "\n")

# Numbers
print("0 :", bool(0))
print("0j:", bool(0j))
print("0.0:", bool(0.0))

# Iterators
print(bool([]))
print(bool([False, None]))
print(bool([1, 2, 3]))

