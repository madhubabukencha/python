"""
In hierarchical inheritance, a single base class is inherited by
multiple child class.
"""


class Parent:
    @staticmethod
    def parent():
        print("I am a parent of 2 children")


class Child1(Parent):
    @staticmethod
    def child1():
        print("I am a child-1")


class Child2(Parent):
    @staticmethod
    def child2():
        print("I am a child-2")


parent_1 = Child1()
parent_2 = Child2()
parent_1.parent()
parent_2.parent()

