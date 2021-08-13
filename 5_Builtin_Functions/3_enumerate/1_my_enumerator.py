"""
The built-in enumerator() method adds a counter to an iterator
and return it in the form of enumerate object. This enumerate
object can then be used directly in for loops or be converted
in to list of tuples using list() method.
"""
my_list = ["Apple", "Mango", "Orange", "Greps"]

enumerate_object = enumerate(my_list)
print("Enumerator Object : {}".format(enumerate_object))

# Converting a list of tuples
print("List of tuples : {}".format(list(enumerate_object)))

# printing using for loop
for number, fruit_name in enumerate(my_list):
    print(f"No : {number} --> {fruit_name}")

# Starting from different index
for number, fruit_name in enumerate(my_list, start=1000):
    print(f"No : {number} --> {fruit_name}")