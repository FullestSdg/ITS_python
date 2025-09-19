from __future__ import annotations

class Film:

    _titolo:str 
    _codice_identificativo:int 

    def __init__(self, title:str, id:int) -> None: 

        if isinstance (title, str) and isinstance(id, int):

            self._titolo = title 
            self._codice_identificativo = id 

        else:
            print("Errore, probabilmente l'id o il titolo non rispecchiano rispettivamente un intero ed una stringa")

    def setID(self, id:int) -> None:

        if isinstance(id, int):
            self._codice_identificativo = id
        
        else:
            print("L'ID inserito non è un intero")

    def setTitle(self, title:str):

        if isinstance(title, str):
            self._titolo = title 
        
        else:
            print("Il titolo del film non è una stringa")

    def getID(self) -> int:
        return self._codice_identificativo 
    
    def getTitle(self) -> str:
        return self._titolo 
    
    def isEqual(self, otherFilm:Film) -> bool: 

        if self.getID() == otherFilm.getID():
            return True 
        
        else:
            return False
        
# film1 = Film("Ciao", 13)
# film2 = Film("Ciao1", 12)

# print(film1.isEqual(film2))
