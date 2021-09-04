"""
The remove() method searches for a given element in the list and
removes first matching element. This method doesn't return anything.
If the given element not found then it will through ValueError.

Syntax:
your_list.remove('element_to_remove')
"""

# Removing element from list
# remove() method going remove first occurrence of element
animal_names = ["Lion", "Cat", "Begal Tigar", "Cat", "Dog"]
print("Original list \t\t\t  :", animal_names)
animal_names.remove("Cat")
print("Updated animal names list :", animal_names)

# Return Value
print(f"Return Value{'':>14}: {animal_names.remove('Dog')}")
# Deleting element which not part of list cause ValueError
# animal_names.remove("Giraffe")
