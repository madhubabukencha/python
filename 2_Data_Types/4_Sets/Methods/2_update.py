"""
The update method adds elements from a set(passed as an argument) to the set
(calling the update method)

Syntax
------
A.update(B)
Here 'A' and 'B' both are sets. Elements of 'B' added to the element of 'A'

NOTE :
This method returns "NONE"
"""

# Updating a set by passing another set as an argument
numbers = {1, 2, 3}
numbers.update({3, 4, 5})
print(numbers)

# Updating a set by passing list as an argument
my_friends = {"Newton", "James"}
my_friends.update(["Ram", "Krishna", "James"])
print(my_friends)

# Updating a set by passing tuple as an argument
my_colleagues = {"Martin", "Anton"}
my_tuple = ("Newton", "Eisenstein")
my_colleagues.update(my_tuple)
print(my_colleagues)

# Updating a set by passing dictionary as an argument
my_colleagues = {"Martin", "Anton"}
my_dictionary = {"Newton": "The scientist", "Ramanujan": "The mathematician"}
my_colleagues.update(my_dictionary)
print(my_colleagues)

# Updating a set by passing string as an argument
even_numbers = {2, 4, 6}
my_string = "8 12 13"
even_numbers.update(my_string)
print(even_numbers)
