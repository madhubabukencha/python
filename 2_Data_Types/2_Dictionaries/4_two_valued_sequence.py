"""
1) We can use the dict() function to convert two-value sequence into a dictionary
2) The first item in each sequence is used as the key and the second as the value
"""


# Dictionary from list of lists
atomic_numbers = [
    ['Calcium', 20],
    ['Helium', 2],
    ['Iron', 26],
    ['Sodium', 11]
]
print(f"From list of lists: {dict(atomic_numbers)}")

# Dictionary from list of tuple
atomic_numbers = [
    ('Calcium', 20),
    ('Helium', 2),
    ('Iron', 26),
    ('Sodium', 11)
]
print(f"From list of tuple: {dict(atomic_numbers)}")

# Dictionary from list of string
atomic_numbers = ["ab", "cd", "ef"]
print(f"From list of strings: {dict(atomic_numbers)}")

# Dictionary from tuple  of strings
atomic_numbers = ("ab", "c3", "ef")
print(f"From tuple of strings: {dict(atomic_numbers)}")