"""
The clear method removes all the elements in a list

Syntax
-----
list.clear()
"""

raw_data = [1, {'name', False}, (1, 3, 4), 1.3334]
print("Before using clear method :", raw_data)
result = raw_data.clear()
print("After using clear method  :", raw_data)
print(f"Result Value {'':>13}: {result}")

# Using delete method to delete all elements
tree_names = ["Bamboo", "Grape Vine", "Neem", "Sandal"]
print("-"*70)
print("Before deleting :", tree_names)
del tree_names[:]
print("After deleting  :", tree_names)