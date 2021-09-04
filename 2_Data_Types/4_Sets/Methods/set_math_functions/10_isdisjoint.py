"""
The isdisjoint() method return True if both sets are disjoint. If not, it return False.
Two sets are said to be disjoint sets if they have no common elements. For example
"""

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
C = {1, 3, 5, 9}

# Both sets have no common elements
print(A.isdisjoint(B))

# Both sets have few common elements
print(A.isdisjoint(C))