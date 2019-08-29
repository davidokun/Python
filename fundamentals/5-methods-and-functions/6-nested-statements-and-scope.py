##########
# SCOPES #
##########

x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# LEGB RULE:
# -Local = Names assigned within a function
# -Enclosing functions locals: In fucntion with  a function
# -Global
# -Built-in: len(), print(), map(), etc

# LOCAL
lambda num: num ** 2  # Var in lambda is local

# Examples

name = 'This is a global string'  # Global definition


def greet():
    name = 'Sammy'  # Enclosing definition

    def hello():
        name = 'Im a local'  # Local definition
        print('Hello ' + name)

    hello()


greet()

###################
#  Global Keyword #
###################
x = 50


def func():
    global x  # Going to affect global definition
    print(f'X is {x}')

    x = 200
    print(f'I just locally changed x to {x}')


func()
print(x)
