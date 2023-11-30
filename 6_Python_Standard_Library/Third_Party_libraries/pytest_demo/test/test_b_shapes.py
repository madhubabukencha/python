"""
In this program we are going to study two important methods of pytest and these are
class based function.

* setup_method:
  This function executed before test function execution.
  So, we can use this to set up required dependence before test
  function call.
* teardown_method:
  Which we be executed after test function,
  if you remove or add anything you can do here.

NOTE: on terminal you have run: pytest -s test_b_shapes.py
-s argument say to print the print statements
For more details read setup_teardown_methods.md
"""
import pytest
from ..source.b_shapes import Circle
import math


class TestCircle:

    def setup_method(self, method):
        print(f"\nExecuting before: {method.__name__}")
        self.circle = Circle(radius=2)

    def teardown_method(self, method):
        print(f"Executing after: {method.__name__}")
        del self.circle

    def test_area(self):
        print(f"\nExecuting: test_area")
        assert self.circle.area() == math.pi * (self.circle.radius ** 2)

    def test_perimeter(self):
        print(f"\nExecuting: test_perimeter")
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
