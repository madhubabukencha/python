"""
These are the basic function based test cases
"""

import pytest
from ..source import a_help_functions as my_functions
import time


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


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(10, 5)
    assert result == 15


@pytest.mark.skip(reason="This feature is currently broken!")
def test_add_2():
    assert my_functions.add(1, 0) == 7


@pytest.mark.xfail(reason="number value should not divided with zero")
def test_divide_2():
    assert my_functions.divide(4, 0)