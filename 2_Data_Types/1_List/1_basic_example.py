"""
In this program we are going to learn basic "list" creation and
accessing list values. A list may have any kind of data type
between square brackets
"""


# Creating an empty list
empty_list = []
print("Empty list    : ", empty_list)

# list with an integer values
list_1 = [1, 2, 3, 4, 6, 7, 8, 9]

# List with string values
list_2 = ["Cow", "Parrot", "Lion"]

# List with string,integer and float values
list_3 = ["cow", 1, 1.6]

# Accessing values in the list
# list_1[inclusive:exclusive]
#  -----------------------
# | H | E | E | L | L | O |
#  -----------------------
# | 0 | 1 | 2 | 3 | 4 | 5 |  --->
#  -----------------------
# |-6|-5 |-4 |-3 |-2 | -1 |  <---
#  -----------------------
print("list_1[1:3]   : ", list_1[1:3])
print("list_2[2]     : ", list_2[1])

# I will print all numbers in a list by adding two index's to
# the current index
print("list_1[::2]   : ", list_1[::2])

# It will print the list in reverse order
print("list_1[::-1]  : ", list_1[::-1])

# Basic operations on List
print("list_1*3      : ", list_1*3)
print("list_1+list_2 : ", list_1 + list_2)

# To check membership of an element
result = 5 in [1, 2, 3, 4, 5]
print("Result        : ", result)



