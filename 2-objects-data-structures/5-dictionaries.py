# Create a dictionary
myDict = {'key1': 'value1', 'key2': 'value2'}
print(myDict)

# Retrieve Value
print(myDict['key2'])

prices = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices['apple'])

# List inside dictionary
d = {'k1': 123, 'k2': [1, 2, 3], 'k3': {'insideKey': 100}}
print(d)

print(d['k2'])
print(d['k2'][1])

b = {'key1': ['a', 'b', 'c']}
myList = b['key1']
letter = myList[2]
print(letter.upper())

# Add new key
c = {'k1': 100, 'k2': 200}
print(c)
c['k3'] = 300
print(c)

# Override value
c['k1'] = 'NEW VALUE'
print(c)

# Methods
c = {'k1': 100, 'k2': 200, 'k3': 300}
# Values only
print(c.values())
# Keys and values
print(c.items())
