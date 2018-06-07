# one.py
# Note: At indentation level 0, all code is run when py file is executed

# When running py file, python does __name__ = "__main__"
if __name__ == "__main__":
    pass


def func():
    print("Func in one.py")


print("Top level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly!")
else:
    print("one.py has being imported!")

