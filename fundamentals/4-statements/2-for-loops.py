# For Loops

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in myList:
    print('Number: {}'.format(item))

# Print even numbers
for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

# Sum

list_sum = 0

for num in myList:
    list_sum += num

print(f'Sum total: {list_sum}')

# Strings

myString = 'Hello World!'
for letter in myString:
    print(letter)

# Tuples
t = (1, 2, 3)

for item in t:
    print(item)

# Tuple unpacking
myListTuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(myListTuples))

for item in myListTuples:
    print(item)

for a, b in myListTuples:
    print(a)
    print(b)

# Dictionaries
print('# Dictionaries #')
dic = {'k1': 1, 'k2': 2, 'k3': 3}

# Iterate over the key
for i in dic:
    print(i)

# print key-values
for i in dic.items():
    print(i)

# Tuple unpacking technique
for key, val in dic.items():
    print(val)

