"""
Fibonacci sequence
"""


def find_fibonacci_iter(max_number):
    """
    Finds the first n fibonacci numbers in the sequence. Iterative.

    :param max_number: the numbers of fibonacci numbers to generate
    :return: a list with the n fibonacci numbers
    """
    fibonacci = [1]

    if max_number == 1:
        return fibonacci

    fibonacci.append(1)

    for i in range(1, max_number - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i - 1])

    return fibonacci


if __name__ == '__main__':
    while True:
        try:
            VALUE = input("Enter number to generate sequence ('q' to quit): ")

            if VALUE == 'q':
                break
            else:
                MAX = int(VALUE)
                print(find_fibonacci_iter(MAX))

        except ValueError:
            print("Enter a positive integer")
