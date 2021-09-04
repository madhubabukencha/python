"""
The add() method of set class adds the element to a set. But if
that element already present then set wouldn't add it and at
the same time it wouldn't through any error

:return:None

NOTE :
add     --> adds the single element at once
update  --> update the multiple element at once
"""

numbers = {1, 2, 3, 4}
numbers.add(5)
print(f"numbers : {numbers}")

# The add method returns the none value
none_value = numbers.add(8)
print(f"none_value : {none_value}, numbers : {numbers}")

# if you are trying add already existing item then it wouldn't
# through an error but simply ignores it
numbers.add(1)
print(f"numbers : {numbers}")

# Adding a tuple to a set
# we wouldn't able add a list,set and dictionary(mutable) to a set
# list, set, dictionary through's "TypeError: unhashable type: 'list/set/dict'"
tuple_numbers = (3, 4, 5)
set_numbers = {5, 6, 9}
set_numbers.add(tuple_numbers)
print(f"set_numbers : {set_numbers}")
