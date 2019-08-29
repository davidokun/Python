# Advance Lists
my_list = [1, 2, 3]

# Add element
print('\n# Add element\n')

my_list.append(4)
my_list.append(4)
print(my_list)

# Count element's occurrences
print('\n# Count element\'s occurrences\n')
print(f'2 = {my_list.count(2)}')
print(f'4 = {my_list.count(4)}')
print(f'5 = {my_list.count(5)}')


# Extend
print('\n# Extend\n')
x = [1, 2, 3]
x.append([4, 5])
print(f'Use append = {x}')

x = [1, 2, 3]
x.extend([4, 5])
print(f'Use Extend = {x}')

# Index
print('\n# Index\n')
print(f'List = {my_list}')
print(f'Index of 2 = {my_list.index(2)}')
print(f'Index of 4 = {my_list.index(4)}')

# Insert
print('\n# Insert\n')
print(f'List = {my_list}')
my_list.insert(2, 'Inserted')
print(f'After insert in pos 2 = {my_list}')
