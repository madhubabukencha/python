"""
The function "filter" filters an iterable by removing items that
don't match with prediction.

Syntax:
------
filter(function, iterable)

Parameters:
Function: It takes function as value and returns value if condition is true.
          If we passed function parameter value is 'None', then it will all
          'true' values.

iterable: iterable which is to be filtered, could be sets, lists, tuples, or containers
          of any iterators
"""
ages = [12, 22, 16, 37, 38]
print("The result of filter function:",
      # Here lambda returning False, True, False, True, True so it returning 22, 37, 38
      list(filter((lambda x: x > 18), ages)))

# Just to see the difference
# map returns a iterable with function result
# Here lambda function result is False, True, False, True, True
result = list(map(lambda x: x > 18, ages))
print("The result of map function: %s" % result)

# As lambda function not returning anything it will
# just return all elements which are not false
print("The result of filter function:",
      list(filter((lambda x: x * 18), ages)))

print("The result of map function:",
      list(map((lambda x: x * 18), ages)))

# For None function case
random_data = [1, 0, True, False, 12, 0, -1, 'a']
print(f'None: {list(filter(None, random_data))}')

