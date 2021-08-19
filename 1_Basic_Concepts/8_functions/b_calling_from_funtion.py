"""
Name : Madhu Babu Kencha
This program will show how to call one function from another function
"""


def function1():
    print("Hey I'm first function")
    # Calling second function in first function
    function2()


def function2():
    print("I am second function")


if __name__ == "__main__":
    function1()
