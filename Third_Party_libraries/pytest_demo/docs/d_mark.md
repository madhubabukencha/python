In Pytest, a "mark" is a way to categorize and tag tests,
which allows you to selectively run specific subsets of tests
based on their marks. Marks are used to add metadata to tests,
and they can be applied to individual test functions or entire
test classes.

Here's a basic overview of how marks work in Pytest:

1. **Marking a Test:**
   You can mark a test by using the `@pytest.mark` decorator.
   This decorator is used to apply various predefined or custom
   marks to your test functions or classes.

   ```python
   import pytest

   @pytest.mark.slow
   def test_example():
       # Test implementation
   ```

   In this example, the `@pytest.mark.slow` decorator marks the
   `test_example` function as a slow test.

2. **Predefined Marks:**
   Pytest provides several predefined marks that you can use out of 
   the box. Some common predefined marks include:
   - `@pytest.mark.skip(reason)`: Skip a test with an optional reason.
   - `@pytest.mark.xfail(condition, reason)`: Expect a test to fail under certain conditions.
   - `@pytest.mark.parametrize(argnames, argvalues)`: Parameterize a test with different sets of input values.

3. **Custom Marks:**
   You can also define your own custom marks by using the `pytest.mark`
   decorator with a name that hasn't been predefined. This can be useful
   for creating your own categorization based on project-specific criteria.

   ```python
   import pytest

   @pytest.mark.my_custom_mark
   def test_custom_mark():
       # Test implementation
   ```

4. **Running Tests with Marks:**
   You can use the `-k` option with Pytest to selectively run tests
   based on their marks. For example, to run only tests marked as
   "slow," you can use:


   ```bash
   pytest -k slow
   ```

   Pytest will identify tests with the specified mark and execute
   only those tests.

5. **Combining Marks:**
   You can also combine multiple marks on a test using logical 
   operators like `and` and `or`:

   ```python
   import pytest

   @pytest.mark.slow and pytest.mark.smoke
   def test_combined_mark():
       # Test implementation
   ```

   This test will be selected if it is marked as both "slow" and
   "smoke."

Marks in Pytest provide a flexible way to organize and control the
execution of your tests, allowing you to run specific subsets of tests
based on criteria that are relevant to your testing needs.

**Examples for mark can be found in below file:**
```commandline
6_Python_Standard_Library/Third_Party_libraries/pytest_demo/test/test_a_help_functions.py
# for parametrized mark concept
6_Python_Standard_Library/Third_Party_libraries/pytest_demo/test/test_square.py
```