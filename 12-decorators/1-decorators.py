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
