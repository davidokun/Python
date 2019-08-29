import unittest
import factorial


class FactorialTest(unittest.TestCase):

    def test_iterative_factorial_of_5(self):
        result = factorial.factorial_iterative(5)
        self.assertEqual(result, 120)

    def test_iterative_factorial_of_10(self):
        result = factorial.factorial_iterative(10)
        self.assertEqual(result, 3628800)

    def test_iterative_factorial_of_0(self):
        result = factorial.factorial_iterative(0)
        self.assertEqual(result, 1)

    def test_recursive_factorial_of_5(self):
        result = factorial.factorial_recursive(5)
        self.assertEqual(result, 120)

    def test_recursive_factorial_of_10(self):
        result = factorial.factorial_recursive(10)
        self.assertEqual(result, 3628800)

    def test_recursive_factorial_of_0(self):
        result = factorial.factorial_recursive(0)
        self.assertEqual(result, 1)
