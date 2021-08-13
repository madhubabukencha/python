"""
Author        : Madhu Babu Kencha
created on    : 15-Nov-2018
last modified : 07-July-2021
"""


# Perimeter of Square
def calculate_perimeter(x):
    return 4*x


# Area of Square
def calculate_area(y):
    return y*y


input_val = int(input('''1.calculate_perimeter
2.calculate_area
Select your function: '''))
assert 0 < input_val < 3, "Entered wrong value"
side_value = int(input("Enter square side value: "))
input_data = {1: "calculate_perimeter(side_value)",
              2: "(calculate_area(side_value))"}

if input_val == 1:
    print(f"If {side_value = } then Perimeter = {eval(input_data[1])}")
elif input_val == 2:
    print(f"If {side_value = } then Area = {eval(input_data[2])}")
