"""
Lets assume we have two sets A and B. If all element of B present in set A then we say
set A is superset of B and A.issuperset(B) method returns True and vice versa.
"""
A = {7, 5, 6, 8, 2, 1, 10}
B = {1, 2, 3, 4, 5, 6, 7, 8}
C = {2, 1, 10}

print(A.issuperset(B))
print(A.issuperset(C))