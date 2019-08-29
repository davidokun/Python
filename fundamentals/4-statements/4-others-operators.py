from random import shuffle
from random import randint

# RANGE FUNCTION ##

# Range from 0 to 9
print('# Range #')
for num in range(10):
    print(num)

# Range from 3 to 9
print('# Range with start#')
for num in range(3, 10):
    print(num)

# Range with steps
print('# Range with step #')
for num in range(0, 11, 2):
    print(num)

# Get a List from a Range
myList = list(range(0, 11, 2))
print(myList)

# ENUMERATE FUNCTION ##
print('# ENUMERATES #')

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcdef'
for item in enumerate(word):
    print(item)

# With tuple unpacking
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# ZIP FUNCTION ##
print('ZIP FUNCTION')

myList1 = [1, 2, 3]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]

for item in zip(myList1, myList2, myList3):
    print(item)

print(list(zip(myList1, myList2, myList3)))

# IN OPERATOR ##
print('\n\n# IN OPERATOR #')

# Check if a value exists in a list
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('a' in 'a world')

# In Dictionaries
print('k1' in {'k1': 123})

d = {'k1': 123}
print(123 in d.values())
print(123 in d.keys())

# MIN,  MAX, Random
print('\n\n# MIN,  MAX, Random #')

myList = [10, 20, 30, 40, 50, 100]
print(min(myList))
print(max(myList))


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)
shuffle(myList)
print(myList)

print(randint(0, 100))

# USER INPUT
print('\n\n# USER INPUT #')

name = input('Whats your name?: ')
print(f'Welcome {name}!!')
