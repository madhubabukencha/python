"""
the := operator gives you a new syntax for assigning variables
in the middle of expressions. This operator is colloquially
known as the walrus operator.
"""
# https://realpython.com/python-walrus-operator/
f = lambda x: x+1
data = [1, 2, 3, 4]
f_data = [y for x in data if (y := f(x)) != 4]
print(f_data)