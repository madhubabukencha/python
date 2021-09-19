"""
1) Similar to the lambda functions which create anonymous functions,
   generator expressions create anonymous generator functions

2) The syntax for generator expression is similar to that of a list
   comprehension in Python. But the square brackets are replaced with
   round parentheses

3) The major difference between a list comprehension and a generator
   expression is that a list comprehension produces the entire list
   while the generator expression produces one item at a time. For this
   reason, a generator expression is much more memory efficient than
   an equivalent list comprehension(Ex: Represent Infinite Stream)
"""


x = 3
# List comprehension
list_compre = [x**2 for x in range(3)]
print(list_compre)

# Generator comprehension
gen_compre = (x**5 for x in range(3))
print(gen_compre)
print(next(gen_compre))
print(next(gen_compre))
print(next(gen_compre))
# Throws stop iteration Error
# print(next(gen_compre))

# Generator expressions can be used as function arguments.
# When used in such a way, the round parentheses can be dropped.
print("Sum: {}".format(sum(x**5 for x in range(3))))
print("Max: {}".format(max(x**5 for x in range(3))))



