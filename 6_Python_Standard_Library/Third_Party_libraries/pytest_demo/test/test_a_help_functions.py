"""
These are the basic function based test cases
"""

import pytest
from ..source import a_help_functions as my_functions


def test_add():
    result = my_functions.add(num_1=4, num_2=6)
    assert result == 10


def test_add_strings():
    result = my_functions.add("Welcome to ", "testing")
    assert result == "Welcome to testing"


def test_divide():
    result = my_functions.divide(num_1=15, num_2=3)
    assert result == 5


def test_divide_zero():
    """
    pytest raises will help us to suppress some know errors
    NOTE: If function raises any new error then this test case will fail
    """
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(num_1=10, num_2=0)
