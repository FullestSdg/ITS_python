from mytypes_azienda1 import RealGEZ
from impiegato import Impiegato
from datetime import date


class Progetto:

    _nome:str # noto alla nascita
    _budget:RealGEZ # noto alla nascita

    def __init__(self, nome:str, budget:RealGEZ) -> None:

        self._nome = nome
        self._budget = budget 
        self.lista_impiegati = []

    def nome(self) -> str:
        return self._nome 
    
    def budget(self) -> RealGEZ:
        return self._budget 
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def set_budget(self, nuovo_budget:RealGEZ) -> None:
        self._budget = nuovo_budget
    
    def add_impiegato(self, impiegato1:Impiegato, data:date) -> None:

        self.data = data
        self.impiegato = impiegato1

        if impiegato1 not in self.lista_impiegati:

            self.lista_impiegati.append(impiegato1)

        else:
            print(f"Errore {impiegato1} è già presente nel progetto")
    
    def remove_impiegato(self, impiegato_da_rimuovere:Impiegato) -> None:
        
        self.impiegato_da_rimuovere = impiegato_da_rimuovere

        if len(self.lista_impiegati) >= 1:

            self.lista_impiegati.remove(impiegato_da_rimuovere)

        elif len(self.lista_impiegati) >= 1 and impiegato_da_rimuovere not in self.lista_impiegati:

            print(f"Errore {impiegato_da_rimuovere} non è nel progetto!")
        
        else:
            raise RuntimeError("Il progetto deve avere almeno un impiegato")