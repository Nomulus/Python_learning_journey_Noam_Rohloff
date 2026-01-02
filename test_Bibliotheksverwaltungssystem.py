from Bibliotheksverwaltungssystem import Library
from Bibliotheksverwaltungssystem import Book

book = Book("Titel", "Autor", "ISBN", True)
library = Library()

def test_Book():
    assert book.title == "Titel"
    assert book.author == "Autor"
    assert book.isbn == "ISBN"
    assert book.is_available == True

def test_Library_():
    library.add_book(book) 