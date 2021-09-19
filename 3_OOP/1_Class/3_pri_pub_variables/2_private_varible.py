"""
a double underscore __ prefixed to a variable makes it private.
It gives a strong suggestion not to touch it from outside the
class(even in sub-class). Any attempt to do so will result
in an AttributeError

Python performs name mangling of private variables. Every member
with double underscore will be changed to _object._class__variable.
If so required, it can still be accessed from outside the class,
but the practice should be refrained
"""


class DataScientist:
    __secret_key = "AAd22AA"

    def __init__(self, experience):
        # Protected variables
        print("Instance Called")
        self.company = "Tata Consultancy Service"
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience
        return self.__experience


class Hire(DataScientist):
    def __init__(self):
        super().__init__(30)

    def display(self):
        # Uncommenting below line cause attribute error.
        # AttributeError: 'Hire' object has no attribute '_Hire__experience'
        # It is telling that accessing private variables out side the class
        # prohibited
        # print(self.__experience)

        # To fix above error try either name mangling or getter and setters
        print(self._DataScientist__experience)


madhu = DataScientist(10)
print(madhu.company)

# Private variables not even accessible from base class
# print(DataScientist.__secret_key)

# Since we can't access private variables out class it throws an AttributeError
# AttributeError: 'DataScientist' object has no attribute '__experience'
# Uncomment below line to see the error
# print(madhu.__experience)

print("Using python name mangling:")
# One way to fix above error is calling private variable with class name
# This called python name mangling
print(madhu._DataScientist__experience)
# We can also modify private variable using name mangling
madhu._DataScientist__experience = 20
print(madhu._DataScientist__experience)

print("Using getter and setter method:")
# Accessing private variable using getter
print(madhu.get_experience())
# Setting private variable value using setter
madhu.set_experience(15)
print(madhu.get_experience())

# Calling private variable from child classl
hire = Hire()
hire.display()