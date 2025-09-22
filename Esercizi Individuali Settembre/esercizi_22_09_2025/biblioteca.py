from libro import Libro 
from studente import Studente

class Biblioteca:

    _available_books:list[Libro]
    _borrowed_books:dict[str, list[Libro]]

    def __init__(self, book_list:list[Libro]) -> None:

        self._available_books = book_list
        self._borrowed_books = {}

    def isAvailable(self, book:Libro) -> bool:

        if book in self._available_books:
            return True
        
        else:
            return False 
        
    def borrowBook(self, book:Libro, studentID:str) -> None:

        if studentID not in self._borrowed_books:

            self._borrowed_books[studentID] = []
            self._borrowed_books[studentID].append(book)

            print(f"Lo studente {studentID} ha preso in prestito {book.getTitle()}")

        else:
            print(f"Il libro {book.getTitle()} non è disponibile!")

    def returnBook(self, book:Libro, studentID:str) -> None:

        if book in self._borrowed_books[studentID]:

            self._borrowed_books[studentID].remove(book)

            self._available_books.append(book)

            print(f"Lo studente {studentID} ha restituito {book.getTitle()}")

        else:
            print(f"{studentID} non possiedo questo libro!")

    def printAvailableBooks(self) -> None:

        for book in self._available_books:
            print(f"{book.info()}")

    def printBorrowedByStudents(self, studentID:str):

        for book in self._borrowed_books[studentID]:
            print(f"{book.info()}")