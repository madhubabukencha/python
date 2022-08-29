"""
Python 3.10, an optional strict parameter was introduced in zip function.
Due to this with if length of two iterable does not match then it will throw a
ValueError.
"""


print("Without strict parameter: ")
for i in zip([1, 2, 3], ["A", "B", "C", "D"]):

    print(i)

print("With strict parameter: ")
for i in zip([1, 2, 3], ["A", "B", "C", "D"], strict=True):
    print(i)
