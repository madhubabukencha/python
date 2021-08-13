"""
The min() method returns a smallest element in an iterable or
smallest of two or more parameters
"""


# Finding the smallest number among the arguments
smallest_number = min(1, 45, 34,23, 67, 100, 1.004)
print(f"The smallest number : {smallest_number}")

# Finding smallest name,(Based on alphabets )
smallest_name = min("Madhu", "Shivani Suryavansi", "Moe", "Meck")
print(f"The smallest name : {smallest_name}")

numbers = min("73", "2", "145", "34")
print(f"Numbers as string : {numbers}")

numbers_with_key = min("73", "2", "145", "34", key=int)
print(f"Numbers with key value as int : {numbers_with_key}")