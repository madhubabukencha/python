import pytest
from ..source.b_shapes import Rectangle


@pytest.fixture
def my_rect():
    # setup part
    rect = Rectangle(10, 20)
    yield rect

    # teardown part(optional)
    del rect


def test_area(my_rect):
    assert my_rect.area() == (10 * 20)


def test_perimeter(my_rect):
    assert my_rect.perimeter() == (2 * 10) + (2 * 20)
