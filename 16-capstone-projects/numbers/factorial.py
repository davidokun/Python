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
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial


def factorial_recursive(num):
    """
    Calculates factorial of a given number
    Uses Recursive approach
    :param num: the number to calculate the factorial
    :return: the factorial result
    """
    if num == 0:
        return 1

    return num * factorial_recursive(num - 1)


if __name__ == '__main__':

    while True:
        try:
            VALUE = int(input("Select option to get Factorial:\n* 1-Iterative\n* 2-Recursive\n=> "))

            if VALUE == 1:
                NUMBER = int(input("(Iterative) Enter positive integer: "))
                print(f'Factorial of {NUMBER} is : {factorial_iterative(NUMBER)}\n')

            if VALUE == 2:
                NUMBER = int(input("(Recursive) Enter positive integer: "))
                print(f'Factorial of {NUMBER} is : {factorial_recursive(NUMBER)}\n')

        except ValueError:
            print('Bye')
            break
