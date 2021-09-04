"""
Creator         : Madhu Babu Kencha
Created on      : 27-10-2018

This programs shows how to remove or delete from dictionary
"""

# The pop() method deletes the specified key-value pair using
# provided 'key' and returns it's value
ranks = {'Madhu': 1, "Ravi": 2, "Kiran": 3}
print("Before pop      :", ranks)
k = ranks.pop('Madhu')
print("After pop       :", ranks)
print("Return value of 'Madhu' : ", k)

# The popitem() method is used delete arbitrary item(key, value)
# It will return 'key' and it's 'value' in tuple format
numbers = {1: 1, 2: 6, 3: 7}
print("Before popitem  :", numbers)
return_value = numbers.popitem()
print("After popitem   :", numbers)
print(f"Return value from popitem: {return_value}")

# Deleting particular elements from the dictionary using key value
del numbers[1]
print("After delete    :", numbers)

# The clear() method will empty the dictionary
numbers.clear()
print("After clear     :", numbers)

# For deleting entire dictionary
del numbers
# Accessing deleted dictionary cause an error
# print(numbers)


