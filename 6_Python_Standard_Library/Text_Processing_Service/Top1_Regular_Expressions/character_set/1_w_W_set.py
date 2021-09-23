"""
Name          : Madhu Babu Kencha
Created on    : 16-01-2019

In this program we will learn usage of character set w and W
"""
import re

# character set "\w" is used match [a-zA-Z0-9_]
print(re.search("\w\w\w\w\w", "man_8kind is a man_8").group())

# "\w" doesn't match symbols other than '_'
print(re)
