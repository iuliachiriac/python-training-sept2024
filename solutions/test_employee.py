import unittest

from solutions.day5_oop_bank_employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John Doe", None, 1000)

    def test_raise_salary_valid_percent(self):
        self.employee.raise_salary(10)
        self.assertEqual(self.employee.salary, 1100)

    def test_raise_salary_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.employee.raise_salary(50)
        self.assertEqual(self.employee.salary, 1000)

    @unittest.skip
    def test_skipped(self):
        pass
