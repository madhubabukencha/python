"""
Creator         : Madhu Babu Kencha
Created on      : 27-10-2018

This program will shows you how to access and update a
dictionary elements.
"""

# Accessing dictionary elements
details = {'name': 'India', 'history': 1200}
print("Accessing through general method :", details['name'])
print("Accessing using get() method     :", details.get('name'))

# Accessing an element which is not present in dict cause an error
# The snippet shows the difference between get() method and normal access
# print("Accessing through general method :", details['age'])
# The get() method returns None if an element not found
# print("Accessing using get() method     :", details.get('age'))

#  Updating and adding new values to dictionary
print("Before adding a dictionary       :", details)
details['history'] = 1333
print("After updating a dictionary      :", details)
details['nature'] = "Cool"
print("After adding new key pair        :", details)
