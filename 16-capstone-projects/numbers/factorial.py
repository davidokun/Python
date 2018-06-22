"""
Get factorial of a given number
"""


def factorial_iterative(num):
    """
    Calculates factorial of a given number
    Uses iterative approach
    :param num: the number to calculate the factorial
    :return: the factorial result
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial


if __name__ == '__main__':

    while True:
        try:
            VALUE = int(input("Select option to get Factorial:\n* 1-Iterative\n=> "))
            if VALUE == 1:
                NUMBER = int(input("Enter positive integer: "))
                print(f'Factorial of {NUMBER} is : {factorial_iterative(7)}\n')
        except ValueError:
            print('Bye')
            break
