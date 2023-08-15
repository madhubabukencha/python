"""
syntax: functools.reduce(function, iterable[, initializer])

Apply function of two arguments cumulatively to the items of iterable,
from left to right, to reduce the iterable to a single value. For
example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
The left argument, x, is the accumulated value and the right argument, y,
is the update value from the iterable. If the optional initializer is present,
it is placed before the items of the iterable in the calculation, and serves
as a default when the iterable is empty. If initializer is not given and
iterable contains only one item, the first item is returned
"""

from functools import reduce

# EXAMPLE-1
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(result)

result = reduce(lambda x, y: x + y, [1, 2, 3, 4], -3)
print(result)
