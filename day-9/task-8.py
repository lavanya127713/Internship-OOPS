class Library:
    def __init__(self, books):
        self.books = books  # list of book names

    def __contains__(self, item):
        return item in self.books


# Creating object
library = Library(["Python", "Java", "C++", "Data Science"])

# Checking membership
print("Python" in library)
print("AI" in library)
