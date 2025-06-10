from types_università1 import CodiceFiscale
from datetime import datetime
from types_università1 import IntGT1900


class Studente:

    _nome:str # noto alla nascita
    _codice_fiscale:CodiceFiscale # {univoco} noto alla nascita
    _data_nascita:datetime # << immutabile >> noto alla nascita
    _anno_iscrizione:IntGT1900 # noto alla nascita
    _matricola:str # {univoco} << immutabile >> noto alla nascita

    def __init__(self, nome:str, codice_fiscale:CodiceFiscale, data_nascita:datetime, anno_iscrizione:IntGT1900, matricola:str) -> None:

        self._nome = nome 
        self._codice_fiscale = codice_fiscale
        self._data_nascita = data_nascita
        self._anno_iscrizione = anno_iscrizione
        self._matricola = matricola 

    def nome(self) -> str:  
        return self._nome 
    
    def codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def data_nascita(self) -> datetime:
        return self._data_nascita
    
    def anno_iscrizione(self) -> IntGT1900:
        return self._anno_iscrizione
    
    def matricola(self) -> str:
        return self._matricola
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome
    
    def set_codice_fiscale(self, nuovo_cf:CodiceFiscale) -> None:
        self._codice_fiscale = nuovo_cf
    
