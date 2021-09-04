"""
The setdefault() method returns the value of the key(if the key is in dictionary)
else it will insert the key with value in the dictionary

syntax:
dictionary.setdefault(key, value)
key   --> key to get value, if key not present then it will insert that in the dictionary
value -->  key with a value default_value is inserted to the dictionary if the key
           is not in the dictionary. If not provided, the default_value will be None.
"""
marks = {'Madhu': 100, 'John': 45, 'Martin': 67}
# if key is present in the dictionary
return_value = marks.setdefault("Madhu", 343)
print(marks)
print(f"If key is present then return value: {return_value} \n")

# if key is not present
return_value = marks.setdefault("Ramana", 343)
print(marks)
print(f"If key is not present then return value: {return_value} \n")

# if key is not present and doesn't set default value
return_value = marks.setdefault("James")
print(marks)
print(f"If key is not present and default value not set then return value: {return_value}")
