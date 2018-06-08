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

print("\n######\n")

# Type errors in Except with finally block
try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")





