# Normal way to get values
print('# Normal way to get values\n')


def create_cubes(num):
    result = []
    for x in range(num):
        result.append(x**3)

    return result


print(create_cubes(10))


# Using generator
print('\n# Using generator\n')


def create_cubes(num):
    for x in range(num):
        yield x**3


for n in create_cubes(20):
    print(n)


def gen_fibon(num):
    a = 1
    b = 1

    for n in range(num):
        yield a
        a, b = b, a + b


for n in gen_fibon(10):
    print(n)

# Using next function to get values
print('\n# Using next function to get values\n')


def simple_gen(n):
    for x in range(n):
        yield x


val = simple_gen(4)

print(next(val))
print(next(val))
print(next(val))
print(next(val))


# Using iter() function
print('\n# Using iter() function\n')

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))



