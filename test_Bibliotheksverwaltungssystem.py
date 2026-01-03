import pytest
from Bibliotheksverwaltungssystem import Library
from Bibliotheksverwaltungssystem import Book

@pytest.fixture 
def book1():
    return Book("Titel", "Autor", "ISBN", True)

@pytest.fixture
def book2():
    return Book("Me and I", "Me", "ABCD", True)

@pytest.fixture
def library_with_two_books(book1, book2):
    lib = Library()
    lib.add_book(book1) 
    lib.add_book(book2) 
    return lib

def test_book_attributes_initialization(book1):
    assert book1.title == "Titel"
    assert book1.author == "Autor"
    assert book1.isbn == "ISBN"
    assert book1.is_available == True

def test_Library_borrow(library_with_two_books, book1):
    library_with_two_books.borrow_book(book1.isbn)
    assert book1.is_available == False

def test_Library_return(library_with_two_books, book1):
    library_with_two_books.borrow_book(book1.isbn)
    library_with_two_books.return_book(book1.isbn)
    assert book1.is_available == True

def test_Library_borrow_unavailable_book(library_with_two_books, book1):
    library_with_two_books.borrow_book(book1.isbn)
    with pytest.raises(ValueError):
        library_with_two_books.borrow_book(book1.isbn)