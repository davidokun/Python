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
