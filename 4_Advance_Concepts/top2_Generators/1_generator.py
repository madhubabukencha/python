"""
1) Creating Generator as easy as defining a normal function but with a
   "yield" statement instead of "return" statement
2) A generator function contains one or more "yield" statements
3) The difference is that while a return statement terminates a function
   entirely, yield statement pauses the function saving all its states and
   later continues from there on successive calls
4) Methods like __iter__() and __next__() are implemented automatically.
   So we can iterate through the items using next().
5) Local variables and their states are remembered between successive calls
6) Finally, when the function terminates, StopIteration is raised automatically
   on further calls
"""


def main():
    n = 1
    print("First call")
    yield n

    n += 1
    print("Second Call")
    yield n

    n += 1
    print("Third call")
    yield n


val = main()
print(next(val))
print(next(val))
print(next(val))
print(next(val))