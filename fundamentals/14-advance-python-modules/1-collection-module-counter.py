"""
Counter:
Count number of occurrences of elements in the array

https://docs.python.org/3.5/library/collections.html#counter-objects
"""

from collections import Counter

my_list = [1, 1, 3, 3, 3, 6, 7, 7, 9, 0]

print(Counter(my_list))

"""
Count letter in a string
"""
s = 'djkshfuawfiafWGFPWrwhwih'
print(Counter(s))

s = "How many times does each word show up in this sentence word word shoe up up"
words = s.split()
print(Counter(words))


c = Counter(words)
print(c.most_common(2))
