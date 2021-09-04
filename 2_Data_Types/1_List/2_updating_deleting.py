# In this program we will see how to update and delete python list values

list1 = ["King", "Queen", 1, 3]
print(f"Original list1:\n{list1}\n")

# updating list values
list1[1:3] = ("Madhu", 7)
print(f"Updated list1[1:3] values:\n{list1}\n")

# Deleting list values
del list1[1]
print(f"After deleting list1[1]:\n{list1}")
