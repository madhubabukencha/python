"""
The symmetric_difference() method returns the symmetric difference of two sets.

The symmetric difference of two sets A and B is the set of elements that are
in either A or B, but not in their intersection(which means not common elements).

or
The symmetric difference will just return the remaining elements after performing
difference between them.
"""
set_A = {1, 2, 4, 5, 7, 8}
set_B = {4, 2, 1, 6, 9, 10}

print(set_A.symmetric_difference(set_B))
print(set_A ^ set_B)

# Just to understand the difference
print(set_A-set_B)
