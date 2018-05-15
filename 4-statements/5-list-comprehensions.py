# List Comprehensions

# Basic approach
myString = 'hello'
myList = []

for letter in myString:
    myList.append(letter)

print(myList)

# Using List Comprehensions
myList2 = [letter for letter in myString]
print(myList2)

myList3 = [x for x in 'word']
print(myList3)

myList4 = [n for n in range(20)]
print(myList4)

myList5 = [n**2 for n in range(10)]
print(myList5)

myList6 = [n for n in range(10) if n % 2 == 0]
print(myList6)

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

results = [x if x % 2 == 0 else 'ODD' for x in range(11)]
print(results)

# With Nested loops
myList = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(myList)
