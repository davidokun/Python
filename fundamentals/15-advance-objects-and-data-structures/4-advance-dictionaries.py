# Advance Dictionaries
d = {'k1': 1, 'k2': 2}

# Dictionary Comprehension
print('\n## Dictionary Comprehension\n')

d1 = {x: x**2 for x in range(10)}
print(d1)

d2 = {k: v**2 for k, v in zip(['a', 'b'], range(2))}
print(d2)

# Iteration over k,v
print('\n## Iteration over k,v\n')
for k in d.keys():
    print(k)

for v in d.values():
    print(v)




