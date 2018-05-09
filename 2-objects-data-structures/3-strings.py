# Single quotes
print('hello')

# Double quotes
print("World")

# Whole string
print("This is a phrase")

# Double and Single quotes
print(" I'm on a run")

# Special
print("Hello \nworld")
print("Hello \tworld")

# Length of a String
print(len("I am Iron Man"))

############
# INDEXING #
############
myString = "Hello World"
print(myString[0])
print(myString[8])

# Negative indexing
print(myString[-1])
print(myString[-5])

###########
# SLICING #
###########
myString = "abcdefghijk"
print(myString)

# myString[start:stop:step]
# From 2 to end
print(myString[2:])

# From Beginning to 3 - Not inclusive
print(myString[:3])

print(myString[3:6])

# Using step
print(myString[::2])

print(myString[2:7:2])

# Reversing a string with step
print(myString[::-1])

#################################
# String Properties and Methods #
#################################

# Immutability
name = "John Doe"
print(name)
# name[0] = "p" # Throw Error

name = "Sam"
print(name)
print('P' + name[1:])

# More concatenation
x = "Hello World"
print(x + " it is good outside")

# Multiplication of letters
letter = "z"
print(letter * 15)

# Methods
x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split())
print(x.split("o"))


