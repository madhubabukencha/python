# Higher order functions take other functions as
# inputs and return them as result


def higher_order(func, arg, status):
    print(status)
    return func(arg)


def multiply_with_two(x):
    return x*2


print("%d" % higher_order(multiply_with_two, 3, "Function result:"))
