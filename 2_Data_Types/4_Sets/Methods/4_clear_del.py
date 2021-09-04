"""
The major difference between del and clear is,
del     --> The del will delete the entire object
clear   --> The clear method just removes the elements of set
"""

# Using "clear" method
countries = {"India", "Italy", "America"}
# The clear method does not return any value
countries.clear()
print(f'countries : {countries}')

# Using "del" function
empty_set_object = set()
del empty_set_object
try:
    print(empty_set_object)
except NameError:
    print("Object was deleted")
