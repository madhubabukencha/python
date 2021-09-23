import timeit

code_to_test = """
numbers = range(1, 1001)
b = []

for number in numbers:
    b.append(number * 2)
"""
# elapsed_time: The amount of time that passes from the
# start of an event to finish its event
elapsed_time = timeit.timeit(code_to_test, number=1)
print(f"elapsed time: {elapsed_time}")
