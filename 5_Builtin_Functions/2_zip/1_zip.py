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

# Converting values to print as set
printable_mapped_set = set(mapped)

print("Zipped iterable set values : ")
print(printable_mapped_set)
