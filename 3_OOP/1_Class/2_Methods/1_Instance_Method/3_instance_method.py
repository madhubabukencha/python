"""
Name : Madhu Babu Kencha
Date : 15-08-2023

What will happen if class attributes and instance variables have same name?
"""


class Train:
    train = "Bharat Express"

    def __init__(self):
        self.train = "Yamuna Express"
        # TypeError: __init__() should return None, not 'str'
        # return train

    def __str__(self):
        return self.train


hyderabad = Train()
# If you are using instance then you are only able to access instance variables
# if comment __init__ method it will also points to class attribute
print(hyderabad.train)

# To access class variable from instance
print(hyderabad.__class__.train)

print(hyderabad)
