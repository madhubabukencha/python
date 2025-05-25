"""
This is a global test file. which contains all global function and
configurations.
"""
import pytest
from ..source.b_shapes import Rectangle


@pytest.fixture
def my_rect():
    # setup part
    rect = Rectangle(10, 20)
    yield rect

    # teardown part(optional)
    del rect
