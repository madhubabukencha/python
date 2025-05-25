"""
This will demo how parameterized mark will work.
Instead of for loops we can use these parameterized concept
"""
import pytest
from ..source.b_shapes import Square


@pytest.mark.parametrize("side_length, expected_area",
                         [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert Square(side_length).area() == expected_area
