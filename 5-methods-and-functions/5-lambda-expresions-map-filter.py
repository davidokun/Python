print('# MAP FUNCTION\n')


# Return the square of a number
def square(num):
    return num**2


# List od numbers
my_nums = [1, 2, 3, 4, 5]

# Use of Map to iterate for each number applying the function square
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


# Define new function
def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))


print('# FILTER FUNCTION\n')


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(check_even, my_nums)))

print('# LAMBDA EXPRESSIONS\n')
# Normal Function


def square(num):
    return num ** 2


# With Lambda
lambda num: num ** 2

res = list(map(lambda num: num ** 2, my_nums))
print(res)

res = list(filter(lambda num: num % 2 == 0, my_nums))
print(res)

res = list(map(lambda name: name[0], names))
print(res)

