# This program explains about usage of list arguments
"""
>>> names=("Madhu", "Kiran", "King")
>>> *names
  File "<stdin>", line 1
SyntaxError: can't use starred expression here
>>> x, *names=("Madhu", "Kiran", "King")
>>> x
'Madhu'
>>> names
['Kiran', 'King']
>>>

>>> l
['97046778', '87678000', '98760979']
>>> *c = l
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> *c, = l
>>> c
['97046778', '87678000', '98760979']

Good Blogs:
https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
"""


def function1():
    # creating a tuple
    # Better to be have more than one element
    x = ("Madhu", "Rama", "Krishna", "Hari", "Narayana")
    # * star is doing un-packing functionality
    function2(*x)


# list arguments had asterisk(*) as their prefix
# list argument is the always last parameter in tuple
# * star is doing packing functionality
def function2(*args):
    # condition true if length is greater than 0
    if len(args):
        for i in args:
            print(i)
    else:
        print("Hello")


if __name__ == "__main__":
    function1()
