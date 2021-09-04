"""
The values method returns a view object with dictionaries values.
values method don't takes any parameter

Syntax:
dictionary.values()
"""

employees_id = {"madhu": 1, "ravi": 2, "kiran": 3}
values = employees_id.values()
print(values)

# Since key method return view object whenever main dictionary
# changed keys dictionary also changes
employees_id.update({"Teja": 4})
print(values)
