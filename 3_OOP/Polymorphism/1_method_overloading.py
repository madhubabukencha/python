"""
Method Overloading means defining more than one method with the same
name and in the same class. It's object's responsibility to pick
relevant method based on arguments passed at time of calling that
method.

Many Object Oriented Programming languages support this without
any problem.

Python also allows you to define multiple methods with the same name in
a class but it remember only last defined method. So if you pass more
arguments than what last method expecting then you will get an error.
"""


class MethodOverloading:

    @staticmethod
    def print_name(name):
        print(f"Your Name: {name}")

    @staticmethod
    def print_name(first_name, last_name):
        print(f"Your Name: {first_name} {last_name}")

    # To fix issue with arguments
    # @staticmethod
    # def print_name(first_name="", last_name=""):
    #     print(f"Your Name: {first_name} {last_name}")


test = MethodOverloading()

test.print_name("Madhu Babu", "Kencha")

# Now we will pass just one argument, it throws an error
# Because it only using second function
test.print_name("Madhu Babu")
