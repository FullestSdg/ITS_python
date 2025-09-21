from film import Film

class Azione(Film):

    _genere:str
    _penale:float

    def __init__(self, title:str, id:int):
        super().__init__(title, id)

        self._genere = "Azione"
        self._penale = 3.00
    
    def getGenere(self) -> str:
        return self._genere 
    
    def getPenale(self) -> float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, giorni_ritardo:int) -> float:
        return giorni_ritardo * self._penale 

class Commedia(Film):

    _genere:str
    _penale:float

    def __init__(self, title:str, id:int):
        super().__init__(title, id)

        self._genere = "Commedia"
        self._penale = 2.50
    
    def getGenere(self) -> str:
        return self._genere 
    
    def getPenale(self) -> float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, giorni_ritardo:int) -> float:
        return giorni_ritardo * self._penale 

class Drama(Film):

    _genere:str
    _penale:float

    def __init__(self, title:str, id:int):
        super().__init__(title, id)

        self._genere = "Drama"
        self._penale = 2.00
    
    def getGenere(self) -> str:
        return self._genere 
    
    def getPenale(self) -> float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, giorni_ritardo:int) -> float:
        return giorni_ritardo * self._penale 

