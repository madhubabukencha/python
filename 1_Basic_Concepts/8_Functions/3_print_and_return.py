"""
In this program we are going to see difference
between "print" and "return" in functions
"""


# function1 shows how print works
def function1():
    print("Hi, welcome")


# function2 shows how return works
def function2():
    k = "Madhu"
    return k


if __name__ == '__main__':
    print(function1())
    print("-"*10)
    print(function2())
