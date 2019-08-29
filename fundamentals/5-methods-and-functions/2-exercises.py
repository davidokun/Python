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


print('## 8.')


def sum_args(*args):
    return sum(args)


print(sum_args(3, 5, 2, 6))


print('## 9.')


def check_even(*args):
    return [n for n in args if n % 2 == 0]


print(check_even(1, 2, 3, 4, 5, 6))


print('## 10.')


def skyline(word):
    result = ''
    index = 1
    for s in word:
        if index % 2 == 0:
            result += s.upper()
        else:
            result += s.lower()

        index += 1

    return result


print(skyline('Anthropomorphism'))


