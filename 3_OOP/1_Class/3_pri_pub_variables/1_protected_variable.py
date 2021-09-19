"""
Name : Madhu Babu Kencha
Date : 02-04-2020

Python's convention to make an instance variable to be a Protected
Variable is to add a prefix underscore('_'). A Protected Variable
means, it effectively prevents it to be accessed, unless it is from
within sub-class.

In fact in python, this doesn't prevent instance variables from
accessing or modifying
"""


class DataScientist:
    def __init__(self, name, experience):
        # Protected variables
        self._name = name,
        self._experience = experience


class Hire(DataScientist):
    def __init__(self, name, experience):
        # Calling Parent class constructor method
        super().__init__(name, experience)

    def print_result(self):
        # Accessing protected variable in sub-class
        if self._experience > 5:
            print("Hired")

    def msc_education(self):
        # modifying protected variable
        self._experience = self._experience+2
        print(self._experience)


employee_1 = Hire("James", 10)
employee_1.print_result()
employee_1.msc_education()

print(employee_1.__dict__)
# Accessing protected variable without any problem
print(employee_1._experience)

# modifying protect variable
employee_1._experience = 15
print(employee_1.__dict__)
