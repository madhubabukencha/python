"""
Lets assume we have two sets A and B. If all element of A present in set B then we say
set A is subset of B and A.issubset(B) method returns True and vice versa.
"""
A = {7, 5, 6}
B = {1, 2, 3, 4, 5, 6, 7, 8}
C = {2, 1, 10}

print(A.issubset(B))
print(C.issubset(B))