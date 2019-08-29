class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # To string() like??
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


my_book = Book('Python in action', 'No way Jose', 230)

print(my_book)
print(str(my_book))
print(len(my_book))


