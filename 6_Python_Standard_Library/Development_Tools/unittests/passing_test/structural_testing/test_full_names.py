"""
Date : 01-07-2019

In this program we are going to create unit test for
"compute.py" functions. To build a test case for a
we need to create a class that need to be inherited from
unittest.Testcase class

Important Points:
Make sure a function name need to start with "test"
(ex: def test_<func_name>, testing_<func_name>)

NOTE: Run in terminal pycharm is not accurate
"""
import unittest
import compute



class TestFullNames(unittest.TestCase):
    def test_full_name(self):
        self.assertEqual(compute.get_full_name("Madhu Babu", "Kencha"), "Madhu Babu Kencha")
        self.assertEqual(compute.get_full_name("Kabir", "Das"), "Kabir Das")
        self.assertEqual(compute.get_full_name("Rabindranath", "Tagore"), "Rabindranath Tagore")

    def testing_compute(self):
        self.assertEqual(compute.addition(4, 4), 8, msg=f"Addition function failed")
        self.assertEqual(compute.addition(-1, 0), -1, msg=f"Addition function failed")
        self.assertEqual(compute.addition(9, -4), 5, msg=f"Addition function failed")

    def test_division(self):
        self.assertEqual(compute.division(10, 5), 2)
        self.assertNotEqual(compute.division(7, 3), 3.5)
        # Testing exceptions
        # self.assertRaises(ZeroDivisionError, compute.division, 10, 0)
        # We are going to achieve this with context manager
        with self.assertRaises(ZeroDivisionError):
            compute.division(10, 0)


# without this if condition pycharm not able to recognize test cases
if __name__ == '__main__':
    unittest.main()
