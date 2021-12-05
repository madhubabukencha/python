"""
In my opinion, I think python wouldn't support multipath.
We can achieve same thing by combining multiple and multilevel
inheritances.

If you still not compromised and you still wanted to implement this
then through base class as last parameter to the derived class.

In this inheritance, a derived class is created from another
derived classes and the same base class of another derived classes.
"""


class TimeWaste:
    _name = "Madhu"

    @staticmethod
    def series():
        print("I eat most of your time if you don't use me wisely")

    @staticmethod
    def display():
        print("I am TimeWast class")


class AmazonPrime(TimeWaste):
    _name = "Amazon"
    @staticmethod
    def prime():
        print("Prime: Yeah!!! A long with entertainment I will provide some benefits")

    @staticmethod
    def display():
        print("I am AmazonPrime class")


class Youtube(TimeWaste):
    _name = "Youtube"
    @staticmethod
    def youtube():
        print("Youtube: It dependents how you train my algorithms")

    @staticmethod
    def display():
        print("I am Youtube class")


# It will through below error if you pass class names like below
#  class Me(TimeWaste, AmazonPrime, Youtube):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases TimeWaste, AmazonPrime, Youtube

class Me(AmazonPrime, Youtube, TimeWaste):
    @staticmethod
    def me():
        print("Me: I am consumer of all three")


person = Me()
person.me()
print(person._name)
person.series()
person.display()

