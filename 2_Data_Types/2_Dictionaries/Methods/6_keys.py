"""
The keys method returns a view object with dictionaries keys.
Keys method don't takes any parameter

Syntax:
dictionary.keys()
"""

employees_id = {"madhu": 1, "ravi": 2, "kiran": 3}
keys = employees_id.keys()
print(keys)

# Since key method return view object whenever main dictionary
# changed keys dictionary also changes
employees_id.update({"Teja": 4})
print(keys)
