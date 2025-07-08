# library_management.py

class Book():
    title = "Thursday's child"
    author = "Napoleon Hill"
    _is_checked_out = True


class Library(Book):
    _books = [
            {"title": "Laws of power", "author": "Napoleon Hill"}, 
            {"title": "ABC guide", "author": "Arthur Eze"}, 
            {"title": "Princess charming", "author":"Walt Disney"}, 
            {"title": "Laws of attraction", "author": "Nap Hill"}, 
            {"title": "Power" , "author": "Universal Pictures"},
            {"title": "Day of reckoning", "author": "Tom Cruise"},
            {"title": "1984", "author": "George Orwell"}
        ]
    
    def __init__(self, title, author):
        self.name = title
        self.author = author

    def add_book(self):
        """Add book to the library"""
        new_book = {"title": "Brave New World", "author": "Aldous Huxley"}
        
        _books.insert(i, new_book)
