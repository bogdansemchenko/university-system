from typing import List, Optional


class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Книга ID: {self.book_id}, Название: '{self.title}', Автор: {self.author}"

class Library:
    def __init__(self):
        self.books: List[Book] = []  # Список всех книг в библиотеке

    def add_book(self, book: Book):
        self.books.append(book)

    def borrow_book(self, book_id: int) -> Optional[Book]:
        book = self.find_book(book_id)
        if book:
            self.books.remove(book)
            return book
        return None


    def find_book(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def __str__(self):
        return f"Библиотека содержит {len(self.books)} книг."