# 1.
def myfunc():
    print('Hello World')


myfunc()


# 2.
def say_hello(name):
    print('Hello {}'.format(name))


say_hello('Jane')


# 3.
def hello_goodbye(value):
    if value:
        return 'Hello'
    else:
        return 'Goodbye'


print(hello_goodbye(True))
print(hello_goodbye(False))


# 4.
def check_boolean(x: bool, y: bool, z: bool):
    if z:
        return x
    else:
        return y


print(check_boolean(True, False, False))
print(check_boolean(False, False, True))


# 5.
def add_numbers(num1: int, num2: int):
    return num1 + num2


print(add_numbers(5, 12))
print(add_numbers(3, 2))


# 6.
def is_even(num: int):
    return num % 2 == 0


print(is_even(2))
print(is_even(3))
print(is_even(25))
print(is_even(30))

print('## 7.')


def is_greater(n1: int, n2: int):
    return n1 > n2


print(is_greater(1, 3))
print(is_greater(5, 2))
print(is_greater(5, 5))