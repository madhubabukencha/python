"""
Name          : Madhu Babu Kencha
Created       : 13-Sep-2018
Last Modified : 02-Jul-2021

Comments in Python start with the character hash(#) and extend to
the end of the physical line. A comment may appear at the start of
a line or following whitespace or code, but not within
a string literal. a hash character within a string literal is just
a hash character.
"""

NUMBER = 1  # The number variable now stores an integer 1
STRING = "Hash/Pound character(#) is used to comment in python"

# Defining comments inside a list(it same with tuple, set and in dictionary)
# As '#' comments the entire physical line, the below line throws an error
# my_list = ['madhu',  # name]

my_list = ['madhu',  # name
           '24'  # age
           , '5180000'  # dummy address
           ]

print(NUMBER)
print(STRING)
print(my_list)
