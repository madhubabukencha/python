"""
Decorator takes function as argument and adds the functionality
and returns it.
"""


def iam_a_decorator(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function


# def ordinary():
#     print("I'm a ordinary function")
#
# ordinary = iam_a_decorator (ordinary)
# ordinary()

# The above entirely commented code equal to below code
@iam_a_decorator
def ordinary():
    print("I'm a ordinary function")


ordinary()
