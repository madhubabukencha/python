# In this program we are going to see how pass arguments


# For function1 we will pass arguments and
# it's values we will pass at time of calling
def function1(x, y, z):
    print("function1 values:", x, y, z)


# In function2 we assign some default values
# to the parameter or arguments
def function2(a, b=0, c=1):
    print("function2 values:", a, b, c)


if __name__ == "__main__":
    function1(2, 3, 4)
    function2(5)
    function2(7, 8)
    # Passing less input than required causes an error
    # function1(1,2)
