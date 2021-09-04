"""
The extend() method extends the list by adding all the items of
a list (which you passed as an argument)  to the end. The extend()
method only modifies the original list but doesn't return any value

syntax:
------
list_1.extend(list_2)

The elements of list_2 will be added at end of list_1
"""

# Extending a list by another list
list_1 = [1, 2, 3, 4, 5]
# output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1.extend(list(range(6, 10)))
print("Extending a list by using another list\t: ", list_1)

list_2 = ["Ram", "Apple", "Parrot"]
# The extend method first split the string into characters and then
# extend the list
string_data = ("James")
list_2.extend(string_data)
print("Extending a list by using a string\t\t: ", list_2)


# Extending data by using tuple values
list_3 = ["Cat", "Ant", "Dog"]
tuple_data = ("Lion", )
list_3.extend(tuple_data)
print("Extending a list by using a tuple\t\t: ", list_3)

