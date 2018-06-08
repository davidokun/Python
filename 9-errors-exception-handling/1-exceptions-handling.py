def add(n1, n2):
    """
    Add two numbers
    :param n1: operand 1
    :param n2: operand 2
    :return: the result of adding operand 1 and operand 2
    """
    print(n1 + n2)


# Try-Except-Else block
try:
    number1 = 10
    number2 = input("Please enter a number: ")
    add(number1, number2)

except:
    print("Look like you aren't adding correctly")
else:
    print("Add went well")



