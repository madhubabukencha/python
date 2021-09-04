"""
The popitem method removes and returns the last element(key, value)
pair inserted into the dictionary. The popitem() doesn't take any
parameters

Syntax:
dict.popitem()
"""
ranks = {'Madhu': 100, "John": 45, "Martin": 67}
print(f"Before delete{'':>10}: {ranks}")
return_value = ranks.popitem()
print(f"After delete{'':>11}: {ranks}")
print(f"Return value{'':>11}: {return_value}")
