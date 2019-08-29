# Tuples: are immutable
myTuple = (1, 2, 3)
myList = [1, 2, 3]

print(type(myTuple))
print(type(myList))

print(len(myTuple))

# Can hold different types, like list
myTuple = ('one', 1, 2.0)
print(myTuple)

# Slicing and indexing
print(myTuple[0])
print(myTuple[-1])

# Find coincidences
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))

