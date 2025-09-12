import unittest
from source_code import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        employee_1 = Employee("Madhu Babu", "Kencha")
        employee_2 = Employee("james", "bond")
        self.assertEqual(employee_1.email, "madhubabu.kencha@email.com")
        self.assertEqual(employee_2.email, "james.bond@gmail.com")


if __name__ == '__main__':
    unittest.main()