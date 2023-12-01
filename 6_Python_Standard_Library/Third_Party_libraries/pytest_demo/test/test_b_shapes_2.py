import pytest
from ..source.b_shapes import Rectangle


@pytest.fixture
def my_rect():
    # setup part
    rect = Rectangle(10, 20)
    yield rect

    # teardown part(optional)
    del Rectangle


def test_area(my_rect):
    assert my_rect.area() == (10 * 20)
