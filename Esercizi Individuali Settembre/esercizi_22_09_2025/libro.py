class Libro:

    _titolo:str 
    _autore:str 
    _anno_pubblicazione:int 

    def __init__(self, title:str, author:str, year:int) -> None:

        if isinstance(title, str) and isinstance(author, str) and isinstance(year, int):

            self._titolo = title 
            self._autore = author 
            self._anno_pubblicazione = year 

        else:
            self._titolo = None 
            self._autore = None 
            self._anno_pubblicazione = None 
            print("Errore, uno dei 3 argomenti non rispecchia il corretto typint")

    def setTitle(self, new_title:str) -> None:

        if isinstance(new_title, str):
            self._titolo = new_title
        
        else:
            print(f"Errore, {new_title} non è una stringa")

    def setAuthor(self, new_author:str) -> None:

        if isinstance(new_author, str):
            self._titolo = new_author
        
        else:
            print(f"Errore, {new_author} non è una stringa")
    
    def setYear(self, new_year:int) -> None:

        if isinstance(new_year, int):
            self._titolo = new_year
        
        else:
            print(f"Errore, {new_year} non è una stringa")
    
    def getTitle(self) -> str:
        return self._titolo
    
    def getAuthor(self) -> str:
        return self._autore 
    
    def getYear(self) -> int:
        return self._anno_pubblicazione

    def info(self) -> None:
        return f"Titolo: {self._titolo}, Autore: {self._autore}, Anno: {self._anno_pubblicazione}"