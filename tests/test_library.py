import unittest
from models.library import Book, Library

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(1, "Программирование на Python", "Иван Иванов")

    def test_book_creation(self):
        self.assertEqual(self.book.book_id, 1)
        self.assertEqual(self.book.title, "Программирование на Python")
        self.assertEqual(self.book.author, "Иван Иванов")

    def test_str_method(self):
        self.assertEqual(str(self.book), "Книга ID: 1, Название: 'Программирование на Python', Автор: Иван Иванов")

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book(1, "Программирование на Python", "Иван Иванов")
        self.book2 = Book(2, "Основы алгоритмов", "Петр Петров")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 2)

    def test_find_book_existing(self):
        book = self.library.find_book(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Программирование на Python")

    def test_find_book_non_existing(self):
        book = self.library.find_book(3)
        self.assertIsNone(book)

    def test_borrow_book_existing(self):
        borrowed_book = self.library.borrow_book(1)
        self.assertIsNotNone(borrowed_book)
        self.assertEqual(borrowed_book.book_id, 1)
        self.assertEqual(len(self.library.books), 1)

    def test_borrow_book_non_existing(self):
        borrowed_book = self.library.borrow_book(3)
        self.assertIsNone(borrowed_book)
        self.assertEqual(len(self.library.books), 2)

    def test_str_method(self):
        self.assertEqual(str(self.library), "Библиотека содержит 2 книг.")