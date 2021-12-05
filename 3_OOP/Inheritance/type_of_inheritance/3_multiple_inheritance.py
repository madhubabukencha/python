"""
MULTIPLE INHERITANCE
--------------------
In Multiple Inheritance, a child class derived from 2 or more
base classes.
"""


class Father:
    @staticmethod
    def father():
        print("Father: I know farming and coding")

    @staticmethod
    def skill():
        print("I know car driving")


class Mother:
    @staticmethod
    def mother():
        print("Mother: I know cooking")

    @staticmethod
    def skill():
        print("I know bike driving")


class Child(Father, Mother):
    @staticmethod
    def child():
        print("Child: I know music")


child = Child()
child.father()
child.mother()
child.child()
# Here it uses Method Resolution Order(MRO)
# Why Father skill method executed instead of Mother class skill method?
# We talk more about in it in future lessons
child.skill()
