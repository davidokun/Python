# While loops
x = 0

while x < 5:
    print(f'Current value of x is: {x}')
    x += 1
else:
    print("X is not less than five")

# Break, Continue, Pass

# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all

# Pass
print('# Pass #')

x = [1, 2, 3]
for i in x:
    pass

# Continue
print('# Continue #')

myString = 'David'

for letter in myString:
    if letter == 'a':
        continue
    print(letter)

# Break
print('# Break #')

myString = 'David'

for letter in myString:
    if letter == 'a':
        break
    print(letter)
