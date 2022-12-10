import unittest

from controllers.controller import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book_1 = Book("The Pact", "Jodi Picoult", "Adult Fiction")
    
    def test_book_has_title(self):
        self.assertEqual("The Pact", self.book_1.title)
    
    def test_book_has_author(self):
        self.assertEqual("Jodi Picoult", self.book_1.author)
    
    def test_book_has_genre(self):
        self.assertEqual("Adult Fiction", self.book_1.genre)
    
    def test_book_has_status(self):
        self.assertEqual(False, self.book_1.checked_out)
