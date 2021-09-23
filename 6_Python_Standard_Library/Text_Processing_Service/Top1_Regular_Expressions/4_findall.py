"""
Name          : Madhu Babu Kencha
Created on    : 15-01-2019

findall pull out the all instances in a string in the form of list

syntax:
re.findall(pattern, string, flags)
"""
import re

# finding all instances in a string
print(re.findall("n|a", "my name is madhu \n babu"))

# multiple characters - literal search
print(re.findall("abcd", "abcdfg abcd"))


