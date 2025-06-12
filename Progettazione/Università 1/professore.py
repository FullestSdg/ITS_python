from types_università1 import CodiceFiscale
from datetime import datetime
from corso import Corso

class Professore:

    _nome:str # noto alla nascita
    _codice_fiscale:CodiceFiscale # {univoco} noto alla nascita
    _data_nascita:datetime # << immutabile >> noto alla nascita
    _insegna:Corso # non noto alla nascita

    def __init__(self, nome:str, codice_fiscale:CodiceFiscale, data_nascita:datetime, insegna:Corso=None) -> None:

        self._nome = nome 
        self._codice_fiscale = codice_fiscale
        self._data_nascita = data_nascita
        self._insegna = insegna

    def nome(self) -> str:  
        return self._nome 
    
    def codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def data_nascita(self) -> datetime:
        return self._data_nascita
    
    def insegna(self) -> Corso:
        return self._insegna
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome
    
    def set_codice_fiscale(self, nuovo_cf:CodiceFiscale) -> None:
        self._codice_fiscale = nuovo_cf