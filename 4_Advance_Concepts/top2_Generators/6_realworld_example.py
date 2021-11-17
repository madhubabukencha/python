"""
Let's say we wanted to print passwords randomly when we
call a function. So, that we can avoid creating passwords
we can use them.
"""
import random
import string as s

letters = s.ascii_letters+s.digits+s.punctuation


def generate_password(letters):
    yield "".join(random.choices(letters, k=14))


for _ in range(10):
    print(next(generate_password(letters)))
