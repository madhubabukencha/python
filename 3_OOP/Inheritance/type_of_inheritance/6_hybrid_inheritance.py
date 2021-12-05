"""
Hybrid Inheritance
------------------
Hybrid Inheritance is a combination of more than one type of inheritance
Ex:
multiple and multilevel
multipath and hierarchical etc..,

Below example is a combination of,
1. Hierarchical Inheritance
2. Multiple Inheritance
"""


class D:
    @staticmethod
    def d():
        print("This is a D class")


class B(D):
    @staticmethod
    def b():
        print("This is a B class")


class C(D):
    @staticmethod
    def c():
        print("This is a C class")


class F(B, C):
    @staticmethod
    def f():
        print("This is a F class")


f = F()
f.d()
f.c()
f.b()
f.f()
