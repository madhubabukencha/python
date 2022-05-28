"""
Date: 23-04-2022
New in version 3.7

The Python breakpoint() built-in function is a tool that allows developers
to set points in code at which a debugger is called. By default, this
function results in an instantiation of Python’s native debugger class

use: 'next' and variable to navigate and see the result respectively
"""


def find_max(numbers):
    # Lowest value
    max_num = -float('inf')
    for number in numbers:
        if number > max_num:
            breakpoint()
            max_num = number
    return max_num


print(find_max([2, 3, 6, 3, 6, 1, 7]))

