def name_function():
    """
    Print 'Hello World' to the console.
    """
    print('Hello World!')


name_function()


def say_hello(name='NAME'):
    """
    Say Hello to someone.

    :param name: the name to say Hello.
    """
    print('Hello {}!'.format(name))


say_hello('Dave')


def add(n1, n2):
    """
    Add two numbers and return the result.

    :param n1: first number
    :param n2: second number
    :return: result of add
    """
    return n1 + n2


result = add(20, 30)
print(result)


def dog_check(my_string):
    return 'dog' in my_string.lower()


print(dog_check('Dog ran away'))
print(dog_check('Cat ran away'))

# PIG LATIN


def pig_latin(word):
    """
    * If word starts with a vowel, add 'ay' to end.

    * If word does not start with a vowel, put first letter at the end, then add 'ay'

    :param word: the word to transform
    :return: the word transformed

    :Example:

        word --> ordway
        apple --> appleay
    """
    first_letter = word[0]
    if first_letter in 'aeiouAEIOU':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


print(pig_latin('word'))
print(pig_latin('apple'))
print(pig_latin('Juice'))
print(pig_latin('Army'))
