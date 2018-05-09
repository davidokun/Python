# List Integers
myList = [1, 2, 3]
print(myList)

# List of different types
myList = ["String", 100, 23.3]
print(myList)

print(len(myList))

# Retrieve by index
myList = ["one", "two", "three"]
print(myList[1])

# Slicing
print(myList[1:])

# Concatenate Lists
myOtherList = ["four", "five"]
print(myList + myOtherList)

# Mutability of a list
newList = myList + myOtherList
print(newList)
newList[0] = "ONE ALL CAPS"
print(newList)

# Adding elements to the end
newList.append("six")
print(newList)

# Remove element from the end of the list
newList.pop()
print(newList)

poppedItem = newList.pop()
print(poppedItem)
print(newList)

# Remove at index
newList.pop(0)
print(newList)

# Sorting
newList = ["a", "e", "x", "b", "c"]
print(newList)
newList.sort()
print(newList)

numList = [3, 5, 1, 0, 8]
print(numList)
numList.sort()
print(numList)

