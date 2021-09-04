""" 
    The map build-in function takes a function and an iterable 
    as an arguments and returns a new iterable with the function
    applied on each argument.

    In other words, map returns a iterable with function result
    
    Syntax 
    ------
    map(function_object, iterable1,iterable2, ...)
"""


def multi_with_two(x):
    return x*2


nums = [1, 2, 3, 4, 5]
print("The result of map function with multiplication 2:",
      # Here function returns 2, 4, 6, 8, 10
      list(map(multi_with_two, nums)))

print("The result of map function with in-build function 'type':",
      list(map(type, nums)))

# With map and lambda expression
print("Result with multiplication 5:",
      list(map(lambda x: x*5, nums)))

# Map operations over a dictionary
dict_1 = [{'name': 'Madhu', 'age': 22, 'id': 1271262},
          {'name': 'Newton', 'age': 23, 'id': 1271272}]
print(list(map(lambda x: x['name'], dict_1)))





