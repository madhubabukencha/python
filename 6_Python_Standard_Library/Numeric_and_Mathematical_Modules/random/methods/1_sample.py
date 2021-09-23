"""
The sample method of random module returns Return a k length list of unique elements
chosen from the population sequence or set. Used for random sampling without replacement.

syntax:
random.sample(population, k)
"""
import string
import random


def user_name():
    population = string.ascii_letters + string.digits + '@$%.'
    username = ''.join(random.sample(population, k=15))
    return username


random_name = user_name()
print(random_name)