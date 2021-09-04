"""
The copy method returns a shallow copy of set
"""
import copy

original_set = {1, 2, 3, 4, 5}
new_copy_set = copy.copy(original_set)
print(f"Id of original_set : {id(original_set)}")
print(f"Id of new_copy_set : {id(new_copy_set)}")

