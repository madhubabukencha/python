"""
The sort() method sorts the element in a list
This method does't return any value

Syntax:
-----
list.sort(key=function_name, reverse=True/False)
"""

# sort() function without any arguments
numbers = [1, 3, 4, 6, 2, 5]
# sort() by default sort in ascending order
numbers.sort()
print(F'Ascending Order : {numbers}')

countries = [1, 32, 23, 12, 45, 2]
# If you pass True to reverse argument it will sort in descending order
result = countries.sort(reverse=True)
print(f"Descending Order: {countries}")
print(f"Return Value    : {result}")


# Function to demonstrate key argument
def remain_of_seven(x):
    return x % 7


random_number = [16, 8, 32, 21]
random_number.sort(key=remain_of_seven)
print(f"Sorting based on return value of func: {random_number}")


# Using build-in len() method
food_menu = ["Rice", "Roti", "Dal", "Sambar"]
food_menu.sort(key=len)
print(food_menu)