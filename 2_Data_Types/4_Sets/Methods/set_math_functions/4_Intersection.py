"""
The intersection() method returns elements which are common in
all sets
See Intersection Image: images/Intersection.png
"""

set_A = {2, 3, 4}
set_B = {3, 4, 6}
set_C = {3, 1, 7}
set_D = {2, 7, 6}

# Now 3 is common in all sets
# Mathematical Representation: (set_A ∩ set_B ∩ set_C)
result = set_A.intersection(set_B, set_C)
print(result)

# Here nothing common among all sets
result = set_A.intersection(set_B, set_C, set_D)
print(result)

# Performing same task using &
result = set_A & set_B & set_C
print(result)
