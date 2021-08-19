"""
In this program we will see how one program returns the other
program output
"""


def first_func():
    def second_func():
        print("Hello World")
    # return second_func()
    return second_func


if __name__ == "__main__":
    print(first_func())
    a = first_func()
    print(a)
