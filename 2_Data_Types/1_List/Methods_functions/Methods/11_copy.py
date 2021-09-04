"""
The copy() method returns a shallow copy of a list

Syntax
------
new_list = list.copy()
"""
# colors
RED = '\033[45m'
END = '\033[0m'

# If you copy a list using '=' operator, new list value will change
# whenever original list value changed
print(RED+"Copying using '=' operator:\t\t"+END)
raw_data = [1, 2, 3, 4]
new_list = raw_data
print("Before updating original list : ", new_list)
raw_data.extend([2])
print("After updating original list  : ", new_list)


print(RED+"Copying using copy() method:"+END)
raw_data = [1, 2, 3, 4]
new_list = raw_data.copy()
print("Before updating original list : ", new_list)
raw_data.extend([2])
print("After updating original list  : ", new_list)

print(RED+"Copying using slicing:\t\t"+END)
raw_data = [1, 2, 3, 4]
new_list = raw_data[:]
print("Before updating original list : ", new_list)
raw_data.extend([2])
print("After updating original list  : ", new_list)
