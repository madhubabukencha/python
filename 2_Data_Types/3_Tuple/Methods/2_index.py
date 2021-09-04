"""
This index() method helps to find the index of an
element

The below program going to find all even number indexes
in the tuple
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in numbers:
    if (number % 2) == 0:
        print(f"Index of {number} : {numbers.index(number)}")

