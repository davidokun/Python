"""
Functions to get prime numbers
"""


def next_prime(number):
    """
    Check is a number is prime or not
    :param number: the number to check
    :return: True if is prime, False if not
    """
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    return is_prime


def list_of_primes(limit):
    """
    Get a list of primes up to limit
    :param limit: maximum number to get primes
    :return: the list of primes up to limit
    """
    primes = []

    for i in range(2, limit + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False

        if is_prime:
            primes.append(i)

    return primes


if __name__ == '__main__':
    OPTION = input("Select option:\n1 - Check number\n2 - Get list of primes\n")

    if OPTION == '1':
        while True:
            try:
                NUMBER_TO_CHECK = int(input("Enter number to check if is prime: => "))
                print(next_prime(NUMBER_TO_CHECK))
            except ValueError:
                break

    if OPTION == '2':
        while True:
            try:
                LIMIT = int(input("Enter max number to get list of primes: => "))
                print(list_of_primes(LIMIT))
            except ValueError:
                break
