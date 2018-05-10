# Getting a file
myFile = open('test.txt')

# Read contents of the file
print(myFile.read())

# Reset cursor to beginning of the file, or else it wont read the file again
myFile.seek(0)
print(myFile.read())

# Read lines and returns a list of lines
myFile.seek(0)
print(myFile.readlines())
myFile.close()

# Accesses file with full filepath
# Windows
# myWinFile = open("C:\\Users\\UserName\\Folder\\test.txt")
# Linux, MacOS
# myLinFile = open("/home/user/folder/test.txt")

# Correct way to open a file. Will auto close the file
with open("test.txt") as myNewFile:
    contents = myNewFile.read()

print(contents)

# Open file in 'read' mode
with open("test.txt", mode='r') as myFile2:
    contents = myFile2.read()

print(contents)

# Append to the file
with open("test.txt", mode='a') as f:
    f.write('\nThis is a four line')

with open("test.txt", mode='r') as f:
    print(f.readlines())

# Create the file if it does'nt exist and override the content each time
with open("new_file.txt", mode='w') as f:
    f.write("I created this file")

with open("new_file.txt") as f:
    print(f.readlines())
