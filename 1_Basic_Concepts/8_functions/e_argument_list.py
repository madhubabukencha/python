"""
Name : Madhu Babu Kencha

This program expains about args parameter

$ names=("Madhu", "Kiran", "King")
$ x, *names=("Madhu", "Kiran", "King")
$ x
'Madhu'
$ names
['Kiran', 'King']
$

$ l
['97046778', '87678000', '98760979']
$ *c = l
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
$ *c, = l
$ c
['97046778', '87678000', '98760979']

Good Blogs:
https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
"""


def function1():
    x = ("Madhu", "Rama", "Krishna", "Hari", "Narayana")
    ip = [195, 30, 0, 345]
    # * star is doing un-packing functionality
    function2(20, 69, *x)
    function3(30, *ip)


def function2(a, c, *args):
    """
    list arguments had asterisk(*) as their prefix
    *args must be a lost argument(only in this case)
    * star is doing packing functionality
    """
    print(a, c)
    for i in args:
        print(i)


def function3(k, *args, n="IP ADDRESS:"):
    print(k, n, sep="\n")
    print(*args, sep=":")

if __name__ == "__main__":
    function1()
