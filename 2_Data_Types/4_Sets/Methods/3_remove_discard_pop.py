"""
In this program we are going to see how to remove an
element using "remove" and "discard" methods

The major difference between remove() and discard() is,
if an element is not present then the discard() wouldn't
through any KeyError but remove() method will do.

The pop() method removes the arbitrary(random) element
"""
friends_names = {"Guido", "Newton", "Ramanujan", "Madhu"}
# Using discard method
friends_names.discard("Madhu")
print(f'friends_names : {friends_names}')

# Using remove method
friends_names.remove("Guido")
print(f'friends_names : {friends_names}')

# Removing an element which is not present using discard()
friends_names.discard("Madhu")

# Removing an element which is not present using remove()
# It through's an error
# friends_names.remove("Madhu")

# Remove method removes the first element from the set
numbers = {1, 2, 3, 4, 5}
print(numbers.pop())
