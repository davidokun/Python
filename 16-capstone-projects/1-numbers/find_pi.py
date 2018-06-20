"""
Find PI to the Nth Digit - Enter a number and have the program generate π (pi)
up to that many decimal places.Keep a limit to how far the program will go.
"""
import math


def find_pi(decimals):
    """
    Calculate PI with 'n' number os decimal places
    :param decimals: number of decimal places in PI
    :return: the value of PI with 'n' decimal places
    """
    precision = f'.{decimals}f'
    return "Pi constant is {r:{p}}".format(r=math.pi, p=precision)


while True:
    try:
        USER_INPUT = input('Please enter decimal places (\'q\' to Quit): ')
        if USER_INPUT == 'q':
            print('Goodbye!')
            break
        else:
            NUMBER = int(USER_INPUT)
            if NUMBER < 1 or NUMBER > 50:
                print("Please enter a number between 1 to 50")
            else:
                print(find_pi(NUMBER))

    except ValueError:
        print('Please enter a positive integer')
