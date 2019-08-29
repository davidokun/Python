"""
namedtuple
Create a new object type creating fields for each element
"""
from collections import namedtuple

# Normal tuple
t = (1, 2, 3)
print(t[0])

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')

print(sam.name)
print(sam[2])

print(sam.breed)
print(sam[1])

