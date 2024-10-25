# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Book is initially available

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to keep track of borrowed books

    def borrow_book(self, book, library):
        if library.check_out_book(book):
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book}")
        else:
            print(f"Sorry, {book} is not available.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.return_book(book)
            print(f"{self.name} has returned {book}")
        else:
            print(f"{self.name} does not have {book} borrowed.")

# Library class
class Library:
    def __init__(self):
        self.books = []  # List of all books in the library

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def check_out_book(self, book):
        if book in self.books and not book.is_checked_out:
            book.is_checked_out = True
            return True
        return False

    def return_book(self, book):
        if book in self.books:
            book.is_checked_out = False
            print(f"{book} is now available in the library.")

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_checked_out]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f" - {book}")
        else:
            print("No books are available at the moment.")

# Testing the Library Management System
# 1. Create a library
library = Library()

# 2. Add books to the library
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
library.add_book(book1)
library.add_book(book2)

# 3. Create a user
user = User("Alex")

# 4. List available books
library.list_available_books()

# 5. Borrow a book
user.borrow_book(book1, library)

# 6. Try to borrow the same book again
user.borrow_book(book1, library)

# 7. List available books after borrowing
library.list_available_books()

# 8. Return the book
user.return_book(book1, library)

# 9. List available books after returning
library.list_available_books()
