# In this program we will see decorator with parameters


def advance_division(func):
    """
    Here you have to notice that parameters of nested inner function
    inside the decorator is same as parameter of functions it decorates
    """
    def inner(a, b):
        print(f'I am going to divide {a} and {b} for {name}')
        if b == 0:
            print("oops! I can't divide as b equal 0")
            return
        # if b ==0 then this return statement wouldn't execute
        return func(a, b)
    return inner


@advance_division
def divide(a, b):
    return a/b


a = divide(4, 5)
print(a)

b = divide(6, 0)
print(b)
