from models.book import Book
# from book import Book

book_1 = Book("The Pact", "Jodi Picoult", "Adult Fiction")
book_2 = Book("The Magic Faraway Tree", "Enid Blyton", "Children's Ficiton")
book_3 = Book("Noughts & Crosses", "Malorie Blackman", "Teen Fiction")

all_books = [book_1, book_2, book_3]

def add_book(title, author, genre):
    new_book = Book(title, author, genre)
    all_books.append(new_book)

def delete_book(list_of_books, list_index):
    list_of_books.pop(list_index)

def update_book_status(list_of_books, list_index, new_status):
    list_of_books[list_index].checked_out = new_status
