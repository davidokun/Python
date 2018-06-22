import unittest
import next_prime_number


class NextPrimeNumber(unittest.TestCase):

    def test_check_prime_number(self):

        prime = next_prime_number.next_prime(3)
        self.assertEqual(prime, True)
        prime = next_prime_number.next_prime(5)
        self.assertEqual(prime, True)

    def test_check_is_not_prime_number(self):

        prime = next_prime_number.next_prime(4)
        self.assertEqual(prime, False)
        prime = next_prime_number.next_prime(8)
        self.assertEqual(prime, False)
        prime = next_prime_number.next_prime(12)
        self.assertEqual(prime, False)
        prime = next_prime_number.next_prime(20)
        self.assertEqual(prime, False)

    def test_get_20_prime_list(self):

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        result = next_prime_number.list_of_primes(30)

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 10)

        for n in range(len(expected)):
            self.assertEqual(result[n], expected[n])
