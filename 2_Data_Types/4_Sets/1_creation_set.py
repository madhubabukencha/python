"""
A set is an unordered collection of items. Since there is no order
among the elements we can't access them using index. sets doesn't
allow duplicate elements in it. So every element must be unique.
Set elements must be immutable but however, the set itself is mutable.
We can add or remove items from it.

Sets can be used to perform mathematical set operations like union,
intersection, symmetric difference etc.

NOTE : The printing order of a set might be change from run to run
"""

# Creating an empty set
# An empty curly braces we use for creating dictionary in python
my_set = set()
print(type(my_set))

my_set = set([1, 2, 3, 4])
print(f'my_set : {my_set}')

# A set may contain different data types
diff_data_type = {123, 23.3456, "Madhu"}
print(f'diff_data_type : {diff_data_type}')

# The main feature of set is, it wouldn't allow duplicates data
unique_countries = {"India", "America", "Russia", "India", "Nepal"}
print(f'unique_countries: {unique_countries}')

# Creating from dictionary
A = {1 : 'a', 2 : 'b'}
print(set(A))