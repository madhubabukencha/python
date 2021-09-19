def fibonacci(num):
    x, y = 0, 1
    for _ in range(num):
        # Yield wouldn't terminate the execution
        # You can see after yield also we have one statements
        yield x
        x, y = y, x+y


def square(nums):
    for num in nums:
        yield num**2


result = square(fibonacci(10))
print([x for x in result])
