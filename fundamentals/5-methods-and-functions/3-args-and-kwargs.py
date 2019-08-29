# Positional arguments
def positional_args(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(positional_args(40, 60))

##
print("\n# Arbitrary number of arguments with *args")
##


# Arbitrary number of arguments with *args
def variable_number_args(*args):
    for i in args:
        print(i)
    return sum(args) * 0.05


print(variable_number_args(20, 50, 40, 10))

##
print("\n# Dictionary of arguments with **kwargs")
##


# Dictionary of arguments with **kwargs
def variable_dictionary_args(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


variable_dictionary_args(fruit='apple', veggie='lettuce')

##
print("\n# Combining *args and **kwargs")


##

# Combining *args and **kwargs
def combining_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


combining_args_kwargs(10, 20, 30, fruit='orange', food='eggs', animal='dog')
