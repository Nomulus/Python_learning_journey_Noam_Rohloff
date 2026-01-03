import pytest
from Bibliotheksverwaltungssystem import Library
from Bibliotheksverwaltungssystem import Book

book = Book("Titel", "Autor", "ISBN", True)
book2 = Book("Me and I", "Me", "ABCD", True)
library = Library()

def test_Book():
    assert book.title == "Titel"
    assert book.author == "Autor"
    assert book.isbn == "ISBN"
    assert book.is_available == True

def test_Library():
    library.add_book(book) 
    library.borrow_book(book.isbn)
    assert library.find_book_by_isbn(book.isbn) == "Titel: Titel\nAutor: Autor\nISBN: ISBN\nAvailable: False\n"