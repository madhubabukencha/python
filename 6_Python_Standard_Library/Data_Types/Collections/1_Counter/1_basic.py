"""
The python's counter is container that will hold the count of each
of the element present in the container.The counter is a sub-class
available inside the dictionary class. Using the Python Counter tool,
you can count the key-value pairs in an object, also called a hash
table object

Good Source: https://www.guru99.com/python-counter-collections-example.html
"""

# Python Counter takes in input a list, tuple, dictionary, string, which are all iterable
# objects, and it will give you output that will have the count of each element

from collections import Counter


text = "The quick brown fox jumps over the lazy dog"
counter = Counter(text)

# This will returns key-value pair with letter and count
print(counter)

# Picking most common two letter
print(f"Most common 2 letters: {counter.most_common(2)}")
