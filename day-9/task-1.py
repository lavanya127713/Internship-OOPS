class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, Price: ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

book1 = Book("Atomic Habits", "James Clear", 450)
book2 = Book("Deep Work", "Cal Newport", 500)

print(book1)
print(book2)

# Printing objects inside a list
books = [book1, book2]
print(books)
