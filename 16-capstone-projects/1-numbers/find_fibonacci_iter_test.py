import unittest
import fibonacci_iter


class FibonacciIterTest(unittest.TestCase):

    def test_1_sequence_number(self):

        result = fibonacci_iter.find_fibonacci_iter(1)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 1)

    def test_first_2_sequence_number(self):

        result = fibonacci_iter.find_fibonacci_iter(2)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 1)

    def test_first_7_sequence_number(self):
        expected_sequence = [1, 1, 2, 3, 5, 8, 13]

        result = fibonacci_iter.find_fibonacci_iter(7)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 7)

        for i in range(7):
            self.assertEqual(result[i], expected_sequence[i])
