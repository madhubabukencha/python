"""
The difference_update() method updates the set, by calling
difference_update() method with the difference of set

For example if we have set 'A' and set 'B', the set difference_
update() method updates the set 'A' with set difference and
returns nothing.
"""
set_A = {2, 5, 8, 9, 3}
set_B = {5, 9, 8}

set_result = set_A.difference_update(set_B)
print(f"set_A : {set_A}")
print(f"set_B : {set_B}")
print(f"set_result : {set_result}")