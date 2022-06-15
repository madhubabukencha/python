from itertools import combinations


pens = ["pen-1", "pen-2", "pen-3", "pen-4", "pen-5"]
# Once combination repeated, that will never repeat again
print(list(combinations(pens, 2)))
