from libro import Libro 

class Studente:

    _nome:str
    _ID:str
    _borrowedbooks:list[Libro]

    def __init__(self, name:str, studentID:str) -> None:

        if isinstance(name, str) and isinstance(studentID, str):
            
            self._nome = name 
            self._ID = studentID 
            self._borrowedbooks = []
        
        else:
            print("Errore, il nome o l'id non sono stringhe!")

    def setName(self, new_name:str) -> None:

        if isinstance(new_name, str):
            self._nome = new_name  

        else:
            print(f"Errore, {new_name} non è una stringa")

    def setID(self, new_id:str) -> None:

        if isinstance(new_id, str):
            self._ID = new_id 

        else:
            print(f"Errore, {new_id} non è una stringa")

    def getName(self) -> str:
        return self._nome 
    
    def getID(self) -> str:
        return self._ID
    
    def addBook(self, book:Libro) -> None:

        if book not in self._borrowedbooks:
            self._borrowedbooks.append(book)
            print(f"Libro: {book.getTitle()} aggiunto con successo!")

        else:
            print(f"Libro: {book.getTitle()} già presente nella lista!")

    def removeBook(self, book:Libro) -> None:

        if book not in self._borrowedbooks:
            print(f"Libro: {book.getTitle()} non è presente nella lista!")
        
        else:
            self._borrowedbooks.remove(book)
            print(f"Libro: {book.getTitle()} rimosso con successo!")

    def printBorrowedBooks(self) -> None:

        for book in self._borrowedbooks:
            print(f"{book.info()}")
