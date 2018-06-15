# Functions return other functions
print("##### Functions return other functions \n")


def hello(name):
    print('The hello() function has been executed!')

    def greet():
        return 'This is the greet() function inside hello'

    def welcome():
        return 'This is the welcome() function inside hello'

    if name == 'greet':
        return greet
    else:
        return welcome


my_new_func = hello('greet')
print(my_new_func())

# Passing functions as parameters
print("\n##### Passing functions as parameters \n")


def hello():
    print("Hello there..")


def other(other_func):
    print("I am other func")
    other_func()


other(hello)

# Using decorators
print("\n##### Using decorators \n")


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before original func')

        original_func()

        print('Some extra code, after original func')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated')


decorated_func = new_decorator(func_needs_decorator)
decorated_func()


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')


func_needs_decorator()
