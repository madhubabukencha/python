"""
The split method break up the a string at specified separator
and returns a list of strings

syntax
------
str.split([separator [, maxsplit]])

separator    This is any deliminator, by default space and newline
maxsplit     Which means maximum numbers of split. The default value
             is -1 which means no limit on the number of splits
"""
text = "I love my country"

# Split at space
print(text.split())

# Split at comma(to avoid space around value give space also)
results = "success, failure, unstable, abort"
print(results.split(", "))

# Split at deliminator which not present in string
print(results.split(": "))

# maxsplit: 2
print(results.split(', ', 2))

# maxsplit: 1
print(results.split(', ', 1))

# maxsplit: 5
print(results.split(', ', 7))

# maxsplit: 0
print(results.split(', ', 0))

##############################
# Enter number separated by space : 45 74 45 884           78
number_data_with_space = input("Enter number separated by space : ")
print(number_data_with_space.split(" "))
print(number_data_with_space.split())