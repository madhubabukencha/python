In Pytest, `setup_method` and `teardown_method` are 
fixture methods that allow you to set up and tear down 
resources for each test method in a class-based test.
These methods are part of the test class and are called
automatically before and after each test method execution.

Here's a brief explanation of each:

1. **`setup_method`**: This method is called before each test method 
in a test class. It is used to set up any resources or perform any
actions that are common to all the test methods in the class.

2. **`teardown_method`**: This method is called after each test
method in a test class. It is used to clean up resources or perform
any actions necessary after the test method has been executed.

Here's a simple example to illustrate their usage:

```python
import pytest

class TestClass:
    def setup_method(self, method):
        # Setup code that should run before each test method
        print(f"\nSetting up for {method.__name__}")

    def teardown_method(self, method):
        # Teardown code that should run after each test method
        print(f"Tearing down after {method.__name__}\n")

    def test_example_1(self):
        print("Executing test_example_1")
        assert 1 + 1 == 2

    def test_example_2(self):
        print("Executing test_example_2")
        assert 2 * 2 == 4

    def test_example_3(self):
        print("Executing test_example_3")
        assert 3 - 1 == 2
```

In this example, the `setup_method` and `teardown_method` methods
are defined within the `TestClass`. The `setup_method` method is
called before each test method, and the `teardown_method` method 
is called after each test method. You can run this test using the
following command:

```bash
pytest -s test_example.py
```

The `-s` flag is used to capture and display the print statements.
When you run this, you'll see output like this:

```
Setting up for test_example_1
Executing test_example_1
.Tearing down after test_example_1

Setting up for test_example_2
Executing test_example_2
.Tearing down after test_example_2

Setting up for test_example_3
Executing test_example_3
.Tearing down after test_example_3
```

This shows the setup and teardown steps happening before and after
each test method in the test class.

**Example code can be found in below file:**
```commandline
6_Python_Standard_Library/Third_Party_libraries/pytest_demo/test/test_b_shapes.py
# for parametrized mark concept
6_Python_Standard_Library/Third_Party_libraries/pytest_demo/test/test_square.py
```