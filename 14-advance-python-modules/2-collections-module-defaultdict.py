"""
Defaultdict

https://docs.python.org/3.5/library/collections.html#defaultdict-objects
"""
from collections import defaultdict

d = {'k1': 1}
print(d.get('k1'))

d = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

# Default values with lambda function
d = defaultdict(lambda: 0)
print(d['one'])
d['two'] = 2
print(d['two'])


d = defaultdict(int)
print(d['Yikes'])
