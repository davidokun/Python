#################
#    Numbers    #
#################

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
result = (((5 * 20) / 2) * 2 + 10 - 10 + 0.25)
print(result)

# What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5))  # 44

# What is the value of the expression 4 * 6 + 5
print(4 * 6 + 5)  # 29

# What is the value of the expression 4 + 6 * 5
print(4 + 6 * 5)  # 34

# What is the type of the result of the expression 3 + 1.5 + 4?
# Float
res = 3 + 1.5 + 4
print(type(res))

# What would you use to find a number’s square root, as well as its square?
# Square root:
r = 100 ** 0.5
print(r)
# Square:
a = 2 ** 2
print(a)

#################
#    Strings    #
#################

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1])

# Reverse the string 'hello' using slicing:
reverse = s[::-1]
print(reverse)

# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

#################
#     Lists     #
#################

# Build this list [0,0,0] two separate ways.

myList1 = [0, 0, 0]
myList2 = [0] * 2

# Reassign 'hello' in this nested list to say 'goodbye' instead:
# list3 = [1,2,[3,4,'hello']]
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

##################
#  Dictionaries  #
##################

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# Grab 'hello'
d = {'simple_key':'hello'}
print(d['simple_key'])

# Grab 'hello'
d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

# Grab hello
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

############
#  Tuples  #
############

# What is the major difference between tuples and lists?
# R: Tuples are immutable

# How do you create a tuple?
t = (1, 2, 'Hello', 1.25, True)
print(type(t))

############
#   Sets   #
############

# What is unique about a set?
# R: They don't accept duplicate elements

# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
mySet = set(list5)
print(mySet)
