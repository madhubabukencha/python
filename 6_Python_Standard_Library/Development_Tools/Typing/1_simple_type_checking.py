"""
We have many mismatched data types and values/return values but,
it does not through any error. To see errors you can do like below:
mypy <absolute_file_path>
"""

name: str = "Madhu Babu Kencha"
# Declaring different data type, it wouldn't through any error
age: str = 26
print(f"{name=}, {age=}")


def add_numbers(a: int, b: float) -> int:
    return a + b


print(add_numbers(2, 5.7))

