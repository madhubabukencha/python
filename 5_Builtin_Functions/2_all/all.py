"""
The all() function returns true only if all elements are true or an iterable
is empty. In an other case it returns False
"""

# IN CASE OF LIST AND TUPLE
print("IN CASE OF LIST AND TUPLE:")
n = [True, True, True]
print(all(n))
m = (True, False, False)
print(all(m))
o = (False, False, False)
print(all(o))
p = (-1, 2, 23)
print(all(p))
q = (0, 0, 0)
print(all(q))
r = []
print(all(r))


# IN-CASE OF STRINGS
print("\nIN-CASE OF STRINGS:")
print(all(""))
# Space also considered as a string but not as an empty string
print(all(" "))
print(all("name"))


# IN-CASE OF DICTIONARY
# In case of dictionary if all are keys(not values) False then only it will return False
print("\nIN-CASE OF DICTIONARY:")
x = {1: 1, 2: '2'}
print(all(x))
print(all({0: 1, False: 2}))
print(all({'0': 2, False: 4}))
# Note difference between them
print(all({'': 2, True: 4}))
print(all({' ': 2, True: 4}))