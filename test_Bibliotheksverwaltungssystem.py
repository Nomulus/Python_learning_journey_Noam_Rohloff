from Bibliotheksverwaltungssystem import Library
from Bibliotheksverwaltungssystem import Book


def test_Book():
    book = Book("Titel", "Autor", "ISBN", True)
    assert book.title == "Titel"
    assert book.author == "Autor"
    assert book.isbn == "ISBN"
    assert book.is_available == True