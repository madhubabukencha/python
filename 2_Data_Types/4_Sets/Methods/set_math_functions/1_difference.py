"""
The difference() method returns the set difference between two sets

If we have two sets 'A' and 'B' then the difference() method returns
the elements which are present in set 'A' but not in set 'B'
See set difference Image: images/difference.png
"""

set_a = {2, 4, 5, 9}
set_b = {4, 5, 9, 7}


set_c = set_a.difference(set_b)
print(f"set difference of A-B : {set_c}")
set_d = set_b.difference(set_a)
print(f"set difference of B-A : {set_d}")
# Which is equal to
# set_d = set_a - set_b

