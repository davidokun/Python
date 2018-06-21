import unittest

import find_pi


class FindPiTest(unittest.TestCase):

    def test_2_decimals(self):
        result = find_pi.find_pi(2)
        self.assertEqual(result, 3.14)

    def test_10_decimals(self):
        result = find_pi.find_pi(10)
        self.assertEqual(result, 3.1415926536)

    def test_30_decimals(self):
        result = find_pi.find_pi(30)
        self.assertEqual(result, 3.141592653589793)

