"""
The purpose of zip() is to map the similar index of multiple containers
so that they can be used just using a single entity

Syntax:
zip(*iterators)

Parameters:
Python iterables or strings(eg:- list, strings)

Return Value:
Returns a single iterator object, having mapped values from all the
containers
"""

# Defining iterables
series = [1, 2, 3, 4]
movie_names = ["Avengers", "Robo", "Silent", "Focus"]
names = ["Madhu Babu", "Rajini", "Chiru", "Prabhas"]

# Using zip() to map iterators
mapped = zip(series, movie_names, names)
# printing zip function result
print(f"Zip function result: {mapped=}")
# Converting values to print as set
printable_mapped_set = set(mapped)

print("Zipped iterable set values : ")
print(printable_mapped_set)

# We will try with some mismatch lists
names = "hel"
numbers = (1, 2, 3, 4, 5)
wishes = ['hi', 'ks', 'ka', 'ta']
result = list(zip(names, numbers, wishes))
print(result)
