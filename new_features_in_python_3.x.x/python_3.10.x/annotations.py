"""
In PEP484 type annotation are introduced. using which we can
specify variable, function and class type exclusively. These
are first introduced in python 3.5. In python3.10 there are
small changes made to this.py
"""
from typing import Union


# Before python 3.10, to specify one or other type
def foo(x: int, y: Union[int, float]) -> Union[int, float]:
    return x*y


# In python 3.10, to specify one or other type
def boo(x: int, y: int | float) -> int | float:
    return x*y


print(foo(3, 4.6))
print(boo(3, 4.6))
