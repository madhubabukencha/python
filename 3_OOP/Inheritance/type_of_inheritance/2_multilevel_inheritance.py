"""
MULTILEVEL INHERITANCE
----------------------
In multi level inheritance a child class derived from parent class
and that parent class is derived from another parent class. This
is just for an example. In real life we might have many multi levels.
"""


class GrandFather:
    @staticmethod
    def grand_father():
        print("GrandFather: I love entire world")


class Father(GrandFather):
    @staticmethod
    def father():
        print("Father: I love only my family")


class Me(Father):
    @staticmethod
    def me():
        print("ME: I love only myself")


# Here you can see, Me class imported features of Father and GrandFather
# futures even without explicitly defined.
hidden_qualities_of_me = Me()
hidden_qualities_of_me.grand_father()
hidden_qualities_of_me.father()
hidden_qualities_of_me.me()
