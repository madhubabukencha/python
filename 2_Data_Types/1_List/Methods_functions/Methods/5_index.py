"""
The index method returns the first occurrence of a
provided element's index

Syntax:
list_with_values.index("element_to_find")
"""
name = list(input("Enter you name :"))
character = input("Enter a character to find : ")
try:
    index = name.index(character)
    print(f"First occurrence of '{character}' at :", index)
except ValueError:
    print("Given character not found in the given name")

