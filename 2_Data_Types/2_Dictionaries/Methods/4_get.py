"""
Name           : Madhu Babu Kencha
Created on     : 31-03-2019

The get() method returns the value of the 'key' if 'key' present is
in the dictionary.

Syntax:
dict.get(key,[value])

key   - key to search in the dictionary
value - value to return if key not found in the dictionary(optional)
        The default value is none
"""

raw_data = {'app': 'Jenkins', 'version': 20.4}

print('app :', raw_data.get('app'))
print('Year :', raw_data.get('year'))

# Using can set default value for key
print('Year :', raw_data.get('year', 0))

# If already value present for key then default value will be ignored.
print('app :', raw_data.get('app', 20))




