# About Conftest.py

The `conftest.py` file in pytest serves a broader purpose than just
storing fixture functions. While fixture functions are commonly defined
in `conftest.py`, it can also contain other configurations and plugins
that affect the behavior of your pytest tests.

Here are some common use cases for `conftest.py`:

1. **Fixture Functions:** As you mentioned, `conftest.py` is commonly
   used to define fixture functions that can be shared across multiple
   test modules.

    ```python
    # conftest.py
    import pytest

    @pytest.fixture
    def my_fixture():
        # fixture setup code
        yield
        # fixture teardown code
    ```

2. **Plugin Registration:** You can use `conftest.py` to register and
   configure plugins that affect the behavior of pytest.

    ```python
    # conftest.py
    def pytest_configure(config):
        config.addinivalue_line("markers", "my_custom_marker: my custom marker")

    # This allows you to use the custom marker in your tests
    # pytest.mark.my_custom_marker
    ```

3. **Hooks:** You can define hooks in `conftest.py` to customize or
   extend the behavior of pytest.
    ```python
    # conftest.py
    def pytest_runtest_setup(item):
        # This hook is called before each test item is set up
        pass
    ```

4. **Shared Fixtures Across Packages:** If you have a test suite with
   multiple packages or modules, `conftest.py` can be  used to define
   fixtures that are shared across those packages.

It's important to note that `conftest.py` is discovered automatically by
pytest. When pytest runs, it collects all `conftest.py` files in the
current directory and its subdirectories and considers them as part of
the test configuration.

In summary, while `conftest.py` is commonly used for defining fixtures,
it is a versatile configuration file that can be used for various
purposes to customize and configure your pytest tests.