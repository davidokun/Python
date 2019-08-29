# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

print('============')

# 2. Use range() to print all the even numbers from 0 to 10
for n in range(0, 11, 2):
    print(n)

print('============')

# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
myList = [n for n in range(1, 51) if n % 3 == 0]
print(myList)

print('============')

# 4. Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(f'Word: "{word}",  is even!!')

print('============')

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the
# number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and
# five print "FizzBuzz".
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

print('============')

# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

myList = [w[0] for w in st.split()]
print(myList)



