"""
list. append(self, object)
--------------------------
The append() method used to add new elements to an existing list
It appends the object to the end of the list
The append() method only modifies the original list and doesn't return any
thing
"""


old_list = [1, 2, 3, 4, 5]
# Appending and element 8 to a list
old_list.append(8)

list_2 = [2, 3, 4, 5, 6]
# Appending a list to a list
list_2.append(["RAM", "KRISHNA"])

# The append() method returns none
# But it will update the list which are trying to append
names = ["James", "Robert", "Newton"]
return_value = names.append("Hitler")
print("Appending an element to list : "+str(old_list))
print("Appending an list to list    : "+str(list_2))
print("Return value from the append : ", return_value)

