# Multiple decorators can be chained in python


def stars(func):
    def inner():
        print("*" * 30)
        func()
        print("*" * 30)
    return inner


def percentage(func):
    def inner():
        print("%" * 30)
        func()
        print("%" * 30)
    return inner

# It equal to
# result = stars(percentage(wish))
@stars
@percentage
def wish():
    print("Hello World")


wish()
