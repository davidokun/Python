import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other term'

for pattern in patterns:
    print('Searching for \"{}\" in : \"{}\"'.format(pattern, text))

    if re.search(pattern, text):
        print('\nMatch was found. \n')
    else:
        print('\nNo Match was found. \n')


# Return of a no match is a None
print(re.search('a', 'b'))

# Match object
match = re.search(patterns[0], text)

print(match.start())
print(match.end())

# Split
split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'

print(re.split(split_term, phrase))

# Find All matches
print(re.findall('hello', 'Here is a hello, and here another hello'))

# PATTERN SYNTAX
print("\n # PATTERN SYNTAX\n")


def multi_re_find(patterns, phrase):
    """
    Takes in a list of regex patterns
    Prints a list of all matches
    :param patterns: list of patterns to check
    :param phrase: string to search for
    """
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')


print("\n## Repetition Syntax\n")
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',          # s followed by zero or more d's
                  'sd+',          # s followed by one or more d's
                  'sd?',          # s followed by zero or one d's
                  'sd{3}',        # s followed by three d's
                  'sd{2,3}',      # s followed by two to three d's
                  ]

multi_re_find(test_patterns,test_phrase)

print("\n## Character Sets\n")
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',     # either s or d
                 's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)

print("\n## Exclusion\n")
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))

print("\n## Character Ranges\n")
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns,test_phrase)

print("\n## Escape Codes")
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
