print("\n# Problem 1\n")
# Handle the exception thrown by the code below by using try and except blocks.


def exponential(numbers):
    """
    Print exponential numbers
    :param numbers: list of numbers
    """
    for i in numbers:
        try:
            print(i**2)
        except TypeError:
            print(f"\"{i}\" is not a valid number.")


exponential(['a', 'b', 'c'])
exponential([2, 3, 4])
exponential([2, "Hi", 4])

print("\n# Problem 2\n")
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'


def divide(n1, n2):
    """
    Divide two numbers
    :param n1: number 1
    :param n2: number 2
    """
    try:
        result = n1 / n2
        print(f"Result is {result}")
    except TypeError:
        print(f"One value is not a number")
    except ZeroDivisionError:
        print(f"Can't divide by zero'")
    finally:
        print(f"All Done\n")


divide(10, 5)
divide(10, "5")
divide(10, 0)

