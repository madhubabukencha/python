"""
The pop() method removes and return the element at a given index
from the list. If the index passed to the pop() method out of range
it return IndexError. The parameter passed to the pop() method is
optional. If no value passed, then it will take -1 by default. Which
means it will removes last element from the list

Syntax:
-----
list.pop(index)
"""

countries = ["America", "China", "Japan", "Tokyo", "India"]
print("Original list \t\t\t\t\t :", countries)
# The pop() method returns an element which going to be delete
flaky_country = countries.pop(3)
print("Return value\t\t\t\t\t :", flaky_country)
print("Updated countries list\t\t\t :", countries)

# pop() method without index removes last value
without_index = countries.pop()
print("pop() method without index value :", countries)
