import random

# Create a generator that generates the squares of numbers up to some number N.
print('\n## Problem 1\n')


def gensquares(N):

    for x in range(N):
        yield x**2


for x in gensquares(10):
    print(x)


# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
print('\n## Problem 2\n')


def rand_num(low, high, n):

    for a in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


# Use the iter() function to convert the string below into an iterator:
print('\n## Problem 3\n')


s = 'Hello!'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


