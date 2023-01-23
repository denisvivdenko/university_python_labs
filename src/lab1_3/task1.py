class Book:
    """
    Class representing a book.
    """
    def __init__(self, author: str, book_name: str, publisher: str, publish_year: int, pages_count: int):
        """
        Initializes a new book instance.
        
        :param author: The author of the book.
        :type author: str
        :param book_name: The name of the book.
        :type book_name: str
        :param publisher: The publisher of the book.
        :type publisher: str
        :param publish_year: The year the book was published.
        :type publish_year: int
        :param pages_count: The number of pages in the book.
        :type pages_count: int
        """
        self._author = author
        self._book_name = book_name
        self._publisher = publisher
        self._publish_year = publish_year
        self._pages_count = pages_count

    @property
    def author(self) -> str:
        """
        The author of the book.
        """
        return self._author

    @author.setter
    def author(self, value: str):
        """
        Set the author of the book.
        
        :param value: The author of the book.
        :type value: str
        :raises ValueError: If value is not a string.
        """
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Author has to be a string")

    @property
    def book_name(self) -> str:
        """
        The name of the book.
        """
        return self._book_name

    @book_name.setter
    def book_name(self, value: str):
        """
        Set the name of the book.
        
        :param value: The name of the book.
        :type value: str
        :raises ValueError: If value is not a string.
        """
        if isinstance(value, str):
            self._book_name = value
        else:
            raise ValueError("Book name has to be a string")

    @property
    def publisher(self) -> str:
        """
        The publisher of the book.
        """
        return self._publisher

    @publisher.setter
    def publisher(self, value: str):
        """
        Set the publisher of the book.
        
        :param value: The publisher of the book.
        :type value: str
        :raises ValueError: If value is not a string.
        """
        if isinstance(value, str):
            self._publisher = value
        else:
            raise ValueError("Publisher has to be a string")

    @property
    def publish_year(self) -> int:
        """
        The year the book was published.
        """
        return self._publish_year

    @publish_year.setter
    def publish_year(self, value: int):
        """
        Set the year the book was published.
        
        :param value: The year the book was published.
        :type value: int
        :raises ValueError: If value is not a positive int.
        """
        if isinstance(value, int) and value > 0:
            self._publish_year = value
        else:
            raise ValueError("Publish year has to be a positive int")
    
    @property
    def pages_count(self) -> int:
        """
        The number of pages in the book.
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, value: int):
        """
        Set the number of pages in the book.
        
        :param value: The number of pages in the book.
        :type value: int
        :raises ValueError: If value is not a positive int.
        """
        if isinstance(value, int) and value > 0:
            self._pages_count = value
        else:
            raise ValueError("Pages count has to be a positive int")



class Library:
    """
    Class representing a library of books.
    """
    def __init__(self, books: list):
        """
        Initializes a new library instance.

        :param books: A list of books in the library.
        :type books: list of Book
        """
        self._books = books

    @property
    def books(self) -> list:
        """
        A list of books in the library.
        """
        return self._books

    @books.setter
    def books(self, array: list):
        """
        Set the books in the library.

        :param array: A list of books.
        :type array: list of Book
        :raises TypeError: If any book in the list is not of type Book.
        """
        for book in array:
            if not isinstance(book, Book):
                raise TypeError("Every book in list has to be of type Book")
        self._books = array

    def get_recent_books(self, author_name: str) -> list:
        """
        Get the books written by the given author that were published since 2010.

        :param author_name: The name of the author.
        :type author_name: str
        :return: A list of books written by the given author that were published since 2010.
        :rtype: list of Book
        """
        result = []
        for book in self.books:
            if book.author == author_name and book.publish_year >= 2010:
                result.append(book)
        return result

    def add_book(self, book: Book):
        """
        Add a book to the library.

        :param book: The book to add.
        :type book: Book
        :raises TypeError: If the book is not of type Book.
        """
        if not isinstance(book, Book):
            raise TypeError("Book has to be of type Book")
        self._books.append(book)

    def remove_book(self, book_name: str):
        """
        Remove a book from the library by its name.

        :param book_name: The name of the book to remove.
        :type book_name: str
        :raises TypeError: If the book name is not of type string.
        """
        temp_list = []
        if not isinstance(book_name, str):
            raise TypeError("Book name has to be of type string")
            
        for book in self.books:
            if book.book_name != book_name:
                temp_list.append(book)
        self.books = temp_list
