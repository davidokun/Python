# Advance Sets methods

s = set()

# Add element
s.add(1)
s.add(2)
s.add(3)
s.add(3)

print(s)

# Clear the Set
s.clear()
print(s)

# Copy Set
s = {1, 2, 3, 4}
sc = s.copy()
sc.add(5)
print(f'Original set: {s}')
print(f'Copied set: {sc}')

# Difference
print(s.difference(sc))
print(sc.difference(s))

# Difference update
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)

# Discard an element
print(s)
s.discard(2)
print(s)

# Intersections
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))

# Intersections update
s1.intersection_update(s2)
print(s1)

# Is Disjoint
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# Is Subset
print(s1.issubset(s2))

# Is Super set
print(s2.issuperset(s1))

# Symmetric difference
print('\n## Symmetric difference\n')
print(s1)
print(s2)
print(s1.symmetric_difference(s2))

# Union
print('\n## Union\n')
print(s1)
print(s2)
print(f'Union = {s1.union(s2)}')
