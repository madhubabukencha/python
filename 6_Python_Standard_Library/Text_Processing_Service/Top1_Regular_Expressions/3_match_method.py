"""
Name          : Madhu Babu Kencha
Created on    : 15-01-2019

Match's only beginning of the string

syntax:
re.match(pattern, string, flags)
"""
import re

# returns none, since 'c' is not at the beginning of the string
print(re.match("c", "abcdfg"))

# returns match object
print(re.match("c", "cabcdfg"))

# bool(None) = false
# bool(object) = true
# To get boolean value
store_bool_value = bool(re.match("c", "abcdfg"))
print(store_bool_value)

# It does works for new line matching
print(re.match("d", "abcef\nd"))

# group() method used to print the match
print(re.match("na", "naThe is a name").group())


