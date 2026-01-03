class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self._isbn = isbn
        self.is_available = is_available

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, value):
        self._isbn = value
    
    def __str__(self):
        return(f"Titel: {self.title}\nAutor: {self.author}\nISBN: {self.isbn}\nAvailable: {self.is_available}\n")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return self.books
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.is_available:
                available_books.append(book)
    
    def borrow_book(self, isbn):
        found_book = False
        for book in self.books:
            if book.isbn == isbn:
                found_book = True
                if book.is_available:
                    book.is_available = False
                else:
                    raise ValueError("Das gewünschte Buch ist bereits verliehen.")
        if not found_book:
            raise ValueError("Das gewünschte Buch ist nicht verfügbar.")

    def return_book(self, isbn):
        found_book = False
        for book in self.books:
            if book.isbn == isbn:
                found_book = True
                if not book.is_available:
                    book.is_available = True
        if not found_book:
            raise ValueError("Das gewünschte Buch ist nicht verfügbar.")
    
    def search_by_author(self, author):
        for book in self.books:
            if book.author.lower() == author.lower():
                return book
        raise ValueError("Das gewünschte Buch ist nicht verfügbar.")

def main():
    book = Book("Titel", "Autor", "ISBN", True)

if __name__ == "__main__":
    main()