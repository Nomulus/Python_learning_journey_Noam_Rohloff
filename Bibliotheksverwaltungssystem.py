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

class Library:
    def add_book(self, book):
        ...
    
    def find_book_by_isbn(self, isbn):
        ...

    def list_available_bookd(self):
        ...
    
    def borrow_book(isbn):
        ...

    def return_book(isbn):
        ...

def main():
    ...

if __name__ == "__main__":
    main()