"""
The __eq__ method in Python is used to define how objects of a
class are compared for equality. The __eq__ method takes two
arguments: self(object on the left-hand side of == operator )
and other(object on the right-hand side of == operator).
__eq__ method always returns a boolean value(True or False).
If it returns something else other than the boolean value it
will lead to TypeError.
"""


class UserVerification:
    """
    Checks if any users have same email and user_name
    """
    def __init__(self, email, user_name):
        self.email = email
        self.user_name = user_name

    def __eq__(self, other):
        if isinstance(other, UserVerification):
            return self.user_name == other.user_name and self.email == other.email
        return False


person1 = UserVerification("abcd@gmail.com", "abcd")
person2 = UserVerification("temp@gmail.com", "temp")
person3 = UserVerification("abcd@gmail.com", "abcd")

if person1 == person3:
    print("Person1 and Person2 have same credentials")

if not (person2 == person3):
    print("Person2 and Person3 have different credentials")