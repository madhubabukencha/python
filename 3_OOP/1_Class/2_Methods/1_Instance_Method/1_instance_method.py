"""
Name : Madhu Babu Kencha
Date : 25-12-2018

Instance method is a method which takes 'self' as it's first argument.
To call an instance method we required an instance.
"""


class Person:

    # Instance attributes
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # Instance methods
    # The methods are called instance methods since these are
    # called on instance object i.e.. in our case it's madhu
    def sings(self, comment):
        return "{0} sings {1}".format(self.name, comment)

    def dance(self):
        return "{} likes dancing".format(self.name)


# Instantiating an object
madhu = Person("Madhu Babu", 22, 5.6)

# Calling instance methods
print(madhu.sings("Nicely"))
print(madhu.dance())

# Since we are calling without an instance it through TypeError
# TypeError: Person.sings() missing 2 required positional arguments: 'self' and 'comment'
# print(Person.sings())
