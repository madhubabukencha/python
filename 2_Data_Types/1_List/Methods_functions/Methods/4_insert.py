"""
Author         : Madhu Babu Kencha
Create on      : 18-01-2019

Syntax:
list_1.insert(index, element)

The insert() method inserts an element to the list_1 at a given index
The insert() method doesn't return anything
"""

# inserting an element
insert_element = [0, 1, 2, 3, 4]
print(f"Original list \t\t\t\t: {insert_element}")
insert_element.insert(5, 5)
print(f"Inserted at the end \t\t: {insert_element}")

# Updating an index(eg: index 1) simply moves already existing
# element to it's right side
insert_element.insert(1, 10)
print(f"Updating an index\t\t\t: {insert_element}")

# Giving an index which greater then the length of the list adds the element
# at the end of list
insert_element.insert(200, 6)
print(f"Giving high index value \t: {insert_element}")

# Inserting a list
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
even_numbers.insert(4, odd_numbers)
print(f"Inserting a list \t\t\t: {even_numbers}")

# Inserting method returns none
values = [1, 2, 3]
ex_values = values.insert(4, 10)
print(f"Return Value{'':>16}: {ex_values}")
