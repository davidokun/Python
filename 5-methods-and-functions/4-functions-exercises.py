# LESSER OF TWO EVENS
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
print('## LESSER OF TWO EVENS: ')


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# ANIMAL CRACKERS:
# Write a function takes a two-word string and returns True if both words begin with same letter
print('## ANIMAL CRACKERS:')


def animal_crackers(animal):
    words = animal.split()
    return words[0][0] == words[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('Krazy Karma'))


# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
print('## MAKES TWENTY: ')


def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    else:
        return n1 + n2 == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print(makes_twenty(30, 2))
print(makes_twenty(30, 20))


# OLD MACDONALD:
# Write a function that capitalizes the first and fourth letters of a name
print('## OLD MACDONALD: ')


def old_macdonald(name):
    return name[0].upper() + \
           name[1:3] + \
           name[3].upper() + \
           name[4:]


print(old_macdonald('macdonald'))
print(old_macdonald('metallica'))
print(old_macdonald('darkside'))
print(old_macdonald('time'))
print(old_macdonald('runaway'))


# MASTER YODA:
# Given a sentence, return a sentence with the words reversed
print('## MASTER YODA: ')


def master_yoda(text):
    list_text = text.split()
    print(" ".join(list_text[::-1]))


master_yoda('I am home')
master_yoda('We are ready')
master_yoda('Powerful you have become')


# ALMOST THERE:
# Given an integer n, return True if n is within 10 of either 100 or 200
print('## ALMOST THERE:')


def almost_there(n):
    return (90 <= n <= 110) or (190 <= n <= 210)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print('## FIND 33:')


def has_33(nums):
    before = 0
    found = False
    for n in nums:
        if before == n:
            found = True
        before = n

    return found


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 3, 1]))


# PAPER DOLL:
# Given a string, return a string where for every character in the original there are three characters
print('## PAPER DOLL: ')


def paper_doll(text):
    res = ''
    for letter in text:
        res += letter * 3

    return res


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print(paper_doll('World'))


# BLACKJACK:
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21, return 'BUST'
print('## BLACKJACK: ')


def blackjack(a, b, c):
    eleven = a == 11 or b == 11 or c == 11
    sum_result = a + b + c

    if sum_result <= 21:
        return sum_result

    adjustment = sum_result - 10

    if sum_result > 21 and eleven:
        return adjustment

    return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print(blackjack(3, 2, 9))
print(blackjack(10, 5, 6))
print(blackjack(10, 5, 7))
print(blackjack(11, 5, 7))


# SUMMER OF '69:
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
print('## SUMMER OF 69:')


def summer_69(numbers):
    total = 0
    for n in numbers:
        if n < 6 or n > 9:
            total += n

    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([5, 4, 3, 2, 1, 6, 8, 7, 9, 10, 11, 12]))


# SPY GAME:
# Write a function that takes in a list of integers and returns True if it contains 007 in order
print("## SPY GAME")


def spy_game(nums):
    zeros = 0
    for n in nums:
        if n == 0:
            zeros += 1
            if zeros <= 2:
                continue
            else:
                zeros -= 1
        elif n == 7:
            return zeros == 2


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 2, 4, 0, 0, 0, 7, 5]))  # True
print(spy_game([1, 2, 4, 0, 0, 0, 7, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
print(spy_game([1, 0, 2, 7, 4, 5, 0]))  # False
print(spy_game([0, 7]))  # False
print(spy_game([7, 7, 7]))  # False
