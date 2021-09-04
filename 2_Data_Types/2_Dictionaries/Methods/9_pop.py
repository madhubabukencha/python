"""
The pop() method removes the provided key as an argument and
returns the value associated with that key. If key is not p-
resent then it will the 'KeyValue' error. If have provided
the default value then it will return that value instead of
error

syntax
dictionary.pop(key, default_value)
key           --> Key to remove
default_value --> If key not found in the dictionary it will return this
                  default value
"""

dictionary = {'Madhu': 100, 'John': 45, 'Martin': 67, 'Ramana': 343}
element = dictionary.pop('Madhu')
print(F"Element that was removed: {element}")
print(f"Dictionary after pop:{dictionary} \n")

# Deleting an element which not present in dictionary
# with default value
element = dictionary.pop('Rajeswari', 200)
print(F"Element that was removed: {element}")
print(f"Dictionary after pop:{dictionary}")

# Deleting an element which not present in dictionary
# without default value
# element = dictionary.pop('Rajeswari')
# print(F"Element that was removed: {element}")