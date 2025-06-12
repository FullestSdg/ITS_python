from datetime import date
from mytypes_azienda1 import RealGEZ

class Impiegato:

    _nome:str # noto alla nascita
    _cognome:str # noto alla nascita
    _nascita:date # noto alla nascita << immutabile >>
    _stipendio:RealGEZ # noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:RealGEZ) -> None:

        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita 
        self._stipendio = stipendio

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome 
    
    def nascita(self) -> date:
        return self._nascita 
    
    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def set_cognome(self, nuovo_cognome:str) -> None:
        self._cognome = nuovo_cognome

    def set_stipendio(self, nuovo_stipendio:RealGEZ) -> None:
        self._stipendio = nuovo_stipendio

    def __repr__(self) -> str:
        return f"Impiegato: {self._nome, self._cognome}"
