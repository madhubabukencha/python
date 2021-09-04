"""
The update() method updates the dictionary with the elements from the another
dictionary object or from an iterable of key/value pairs.
update() method adds element(s) to the dictionary if the key is not in the
dictionary. If the key is in the dictionary, it updates the key with the new value.
"""
numbers = {'madhu': 10, 'James': 230, 'kiran': 45, 'rs': 500, 'as': 12}

# update already existing key value
dict_object = {'madhu': 200}
numbers.update(dict_object)
print(numbers)

# Adding new key
dict_object = {'Jamesss': 23}
numbers.update(dict_object)
print(numbers)

# Updating through tuple
numbers.update(x=25, y=100)
print(numbers)

