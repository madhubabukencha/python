"""
Name             : Madhu Babu Kencha
Created on       : 25-02-2019

The clear() method removes all the elements inside a dictionary.
It doesn't take any parameter. It doesn't return any value.
"""

raw_data = {"name": 'Madhu Babu Kencha', "date": '13-05-1996'}
print(F"The raw data\t\t\t\t : {raw_data}")

# The clear method returns none
return_value = raw_data.clear()
print("After using clear() method \t :", raw_data,
      "\nReturn value\t\t\t\t :", return_value)

# We can also empty the dictionary by assigning empty curly braces
vowels = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
print("Before using curly braces \t :", vowels)
vowels = {}
print("After assigning curly braces :", vowels)

# Difference between using clear method and assign curly braces
numbers = {'one': 1, 'two': 2, 'three': 3}
dummy = numbers
# It seems clear method clearing all element in all copies
numbers.clear()
print("After using clear method\t :", dummy)

numbers = {'one': 1, 'two': 2, 'three': 3}
dummy = numbers
numbers = {}
print("After using curly braces\t :", dummy)
