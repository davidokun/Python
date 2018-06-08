# Problem 1
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

