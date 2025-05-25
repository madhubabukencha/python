"""
In Python, a dataclass is a class primarily designed to hold data.
It's a way to automatically generate boilerplate code for classes
that mainly consist of attributes. Introduced in Python 3.7, dataclasses
simplify the creation of such classes by providing default implementations
for common methods like __init__, __repr__, __eq__, and others, based on
the class attributes you define.
"""
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    genre: str = 'Fiction'
    is_available: bool = True

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
book2 = Book("Pride and Prejudice", "Jane Austen", 432, "Romance")
book3 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)

print(book1)
print(book2)
print(book1.genre)

# Automatic  __eq__ verification
print(book1 == book3)