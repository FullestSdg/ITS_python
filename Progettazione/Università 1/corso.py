from types_università1 import RealGTZ

class Corso:

    _nome:str # noto alla nascita
    _codice:str # {univoco} << immutabile >> noto alla nascita
    _durata_ore:RealGTZ # noto alla nascita

    def __init__(self, nome:str, codice:str, durata_ore:RealGTZ) -> None:

        self._nome = nome 
        self._codice = codice
        self._durata_ore = durata_ore

    def nome(self) -> str:  
        return self._nome 
    
    def codice(self) -> str:
        return self._codice
    
    def durata_ore(self) -> RealGTZ:
        return self._durata_ore
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome
    
    def set_durata_ore(self, nuova_durata_ore:RealGTZ) -> None:
        self._durata_ore = nuova_durata_ore