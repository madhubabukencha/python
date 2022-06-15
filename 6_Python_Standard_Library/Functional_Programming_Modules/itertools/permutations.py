"""
Permutations are different ways of arranging objects in a definite order
"""
from itertools import permutations

pens = ["pen-1", "pen-2", "pen-3", "pen-4", "pen-5"]
# We have 5 pens, check possibilities of picking one pen.
# So, he might pick [('pen-1',), ('pen-2',), ('pen-3',), ('pen-4',), ('pen-5',)]
# Therefore we have 5 permutations
print(list(permutations(pens, 1)))

# We have 5 pens, check possibilities of picking 2 pens from 5 pens
# formula: n!/(n-r)!,
# n = total number of pens, r = number of pens to pick
print(list(permutations(pens, 2)))

