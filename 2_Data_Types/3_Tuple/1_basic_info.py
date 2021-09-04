"""
Tuple are as same as list. The difference between two data type was
we can't able to change the elements of tuple once they have assigned.

Basic Data about tuple
----------------------
>>> tuple_1 = ()
>>> type(tuple_1)
<class 'tuple'>
>>> tuple_2 = " "
>>> type(tuple_2)
<class 'str'>
>>> tuple_3 = ("James")
>>> type(tuple_3)
<class 'str'>
>>> tuple_4 = ("James",)
>>> type(tuple_4)
<class 'tuple'>
>>>
"""

# Defining an empty tuple
empty_tuple = ()

# Defining a tuple.
names = ("Ram", "Sita", "Lakshman")
print(names)

# Accessing tuple values
print(names[0])

# We can also access values using slicing
print(names[1:])

# Extending a tuple
print(names + ("madhu", "Sita"))

# Modifying tuple values causes an error
# TypeError: 'tuple' object does not support item assignment
# names[0] = "The god"

