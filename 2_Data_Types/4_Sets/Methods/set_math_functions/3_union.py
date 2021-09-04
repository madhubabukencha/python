"""
The Python set union() method returns a new set with distant elements from data sets
See Union Image: images/Union.png
"""
set_a = {1, 2, 'a'}
set_b = {2, 3, 'b'}
set_c = {4, 3, 'c'}
set_d = {'a': 24, 'd': None}
print(set_a.union(set_b).union(set_c).union(set_d))
print(set_a | set_b | set_c | set(set_d))
print(set.union(set_a, set_b, set_c, set_d))
