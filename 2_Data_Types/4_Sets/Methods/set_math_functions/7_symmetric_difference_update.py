"""
Let's assume we have two sets "A" and "B". The A.symmetric_difference_update(B) method
updates the set A with elements which are in either A or B, but not in their intersection.
"""

set_A = {2, 22, 12, 23, 1, 3}
set_B = {100, 12, 3, 121, 2323}

# Here 3 ,12 are common in both sets, those wouldn't get updated in set_A
set_A.symmetric_difference_update(set_B)
print(set_A)