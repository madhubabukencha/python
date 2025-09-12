"""
Last Updated: 12-Sep-2025
Author: Madhu Babu Kencha

What are TypedDicts?
TypedDicts are a feature in Python's typing module that allows
you to define dictionaries with a specific structure, where the
keys are strings and the values can be of different types. This is
particularly useful for type checking and ensuring that dictionaries
conform to a certain schema. They were introduced in PEP 589 and are
available in Python 3.8 and later versions.

Benefits of Using TypedDicts:
- Type Safety: Helps catch type-related errors during development.
- Improved Readability: Makes it clear what structure a dictionary should have.
- Better Tooling Support: Enhances the capabilities of type checkers and IDEs.

Checking with Mypy:
$ mypy typeddict.py
"""

from typing import TypedDict, NotRequired, Required


# Defining a TypedDict for a user profile
class UserProfile(TypedDict):
    username: str
    email: str
    age: NotRequired[int]  # Optional field
    is_active: Required[bool]  # Required field


# Creating an instance of UserProfile
user1: UserProfile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 30,
    "is_active": True
}

user2: UserProfile = {
    "username": "jane_doe",
    "email": "jane@example.com",
    "is_active": False
}  # age is optional


# Code which would raise a type checker error
user3: UserProfile = {
    "email": "invalid_email",
    "age": "not_a_number",
    "is_active": "yes"
}  # Missing required field 'username' and wrong types for 'age' and 'is_active'
