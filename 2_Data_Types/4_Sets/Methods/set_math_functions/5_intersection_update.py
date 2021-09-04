"""
The intersection_update() method update the set by calling intersection_update()
method with the intersection of sets.

set.intersection_update(*sets)
"""
set_A = {1, 2, 3, 4, 5}
set_B = {6, 7, 1, 5, 10}
set_C = {4, 1, 5, 12, 13, 14}
print(set_A)
set_A.intersection_update(set_B, set_C)
print(set_A)


