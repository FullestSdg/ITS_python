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
    
    def iscoinvolto(self, impiegato:Impiegato) -> bool:

        self.impiegato = impiegato

        if self.impiegato in self.lista_impiegati:
            return True
        
        else:
            return False
    
    def remove_impiegato(self, impiegato_da_rimuovere:Impiegato) -> None:
        
        self.impiegato_da_rimuovere = impiegato_da_rimuovere

        if len(self.lista_impiegati) >= 1:

            self.lista_impiegati.remove(impiegato_da_rimuovere)

        elif len(self.lista_impiegati) >= 1 and impiegato_da_rimuovere not in self.lista_impiegati:

            raise ValueError(f"Errore {impiegato_da_rimuovere} non è nel progetto!")
        
        else:
            raise RuntimeError("Il progetto deve avere almeno un impiegato")
        
    def check_ultimo_impiegato(self) -> Impiegato:

        if len(self.lista_impiegati) >= 1:

            return self.lista_impiegati[-1]
        
        else:
            raise RuntimeError("Il progetto deve avere almeno un impiegato")


