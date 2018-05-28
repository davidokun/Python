# Write a function that computes the volume of a sphere given its radius.
print("# VOLUME OF A SPHERE\n")


def vol(rad):
    volume = (rad**3 * 3.141592) * (4/3)
    return "Volume of Sphere with radius {1} is = {0:1.5f} m3".format(volume, rad)


print(vol(2))
print(vol(8))

# Write a function that checks whether a number is in a given range (inclusive of high and low)
print("\n# NUMBER IS IN RANGE\n")


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return '{0} is in the range between {1} and {2}'.format(num, low, high)
    else:
        return '{0} is NOT in the range between {1} and {2}'.format(num, low, high)


print(ran_check(5, 2, 7))
print(ran_check(3, 1, 10))
print(ran_check(10, 1, 10))
print(ran_check(1, 1, 10))
print(ran_check(50, 15, 30))
print(ran_check(0, 15, 31))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
print("\n# CALCULATES THE NUMBER OF UPPER CASE LETTERS AND LOWER CASE LETTERS\n")


def up_low(sentence):
    upper = 0
    lower = 0
    for s in sentence:
        if s.islower():
            lower += 1
        if s.isupper():
            upper += 1

    print('No. of Upper case characters : {}'.format(upper))
    print('No. of Lower case characters : {}'.format(lower))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
s2 = 'May the Force Be with YoU!'
up_low(s2)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
print("\n# RETURNS A NEW LIST WITH UNIQUE ELEMENTS\n")


def unique_list(my_lst):
    return list(set(my_lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(unique_list([1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 8, 9, 0, 0]))


# Write a Python function to multiply all the numbers in a list.
print("\n# MULTIPLY ALL THE NUMBERS IN A LIST\n")


def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n

    return result


print(multiply([1, 2, 3, -4]))
print(multiply([4, 0, 5, 10, 2]))
print(multiply([4, 3, 5, 10, 2]))


# Write a Python function that checks whether a passed in string is palindrome or not.
print("\n# CHECKS WHETHER A PASSED IN STRING IS PALINDROME OR NOT\n")


def palindrome(word):
    lower_word = word.lower().replace(' ', '')
    return lower_word == lower_word[::-1]


print(palindrome('helleh'))
print(palindrome('madam'))
print(palindrome('May the force be with you'))
print(palindrome('nurses run'))
print(palindrome('Sometamos o matemos'))
print(palindrome('Yo dono rosas oro no doy'))
print(palindrome('Do or do not there is no try'))
