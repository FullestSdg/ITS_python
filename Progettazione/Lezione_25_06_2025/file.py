from datetime import date
from abc import ABC, abstractmethod

class Persona(ABC):

    _nome: str

    @abstractmethod
    def __init__(self, nome:str) -> None:
        self.set_nome() = nome
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome 
    

class Studente(Persona):

    _matricola:int 

    def __init__(self,nome:str, matricola:int) -> None:
        super().__init__(nome)

        self.set_matricola() = matricola 

    def set_matricola(self, matricola:int) -> None:
        self._matricola = matricola 

    def matricola(self) -> int:
        return self._matricola

class Docente(Persona):

    _nascita:date

    def __init__(self,nome:str, nascita:date) -> None:
        super().__init__(nome)

        self.set_nascita() = nascita

    def set_nascita(self, nascita:date) -> None:
        self._nascita = nascita

    def nascita(self) -> date:
        return self._nascita