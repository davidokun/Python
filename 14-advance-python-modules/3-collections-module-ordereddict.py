"""
OrderedDict
Retain insertion order of dict elements
"""
from collections import OrderedDict

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

for k, v in d.items():
    print(k, v)

print("\n# With Ordered Dict\n")
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8

for k, v in d.items():
    print(k, v)


# d1 = {}
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

# d2 = {}
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)
