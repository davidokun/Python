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

