"""
Author              : Madhu Babu Kencha
Created on          : 18-01-2019

Syntax
-----
all(iterable)
The all() method returns True when all elements in the given iterable are true.
if not, it return false

All values are True                   --> True
All values are false                  --> False
One value is True(others are false)   --> False
One value is False(other are True)    --> False
Empty iterable                        --> True
"""
# All values are true
list_values = [1, 2, 3, 4, "Came Roon"]
print(all(list_values))

# All values are false
list_values = [False, 0]
print(all(list_values))

# one value is false
list_values = [1, 2, 3, 0]
print(all(list_values))

# one true value
one_true = [0, False, 5]
print(all(one_true))

# empty iterable
empty_iterable = []
print(all(empty_iterable))
