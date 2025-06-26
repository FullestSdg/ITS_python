from impiegato import Impiegato
from dipartimento import Dipartimento
from progetto import Progetto 
from datetime import date

class Direzione:

    class _link:

        _direttore:Impiegato #noto alla nascita
        _dipartimento:Dipartimento #noto alla nascita

        def __init__(self, direttore:Impiegato, dipartimento:Dipartimento) -> None:

            self._direttore = direttore
            self._dipartimento = dipartimento

        def setDirettore_Dipartimento(self, direttore:Impiegato, dipartimento:Dipartimento) -> None:
            
            self._dipartimento = dipartimento
            self._direttore = direttore 
            self.dict_direttori:dict[Impiegato,Dipartimento] = {}

            self.dict_direttori[direttore] = dipartimento          

        def is_direttore(self, direttore:Impiegato) -> bool:
            self._direttore = direttore 

            if direttore in self.dict_direttori:
                return True 
            
            else:
                return False

        def direttore(self) -> Impiegato:
            return self._direttore
        
        def dipartimento(self) -> Dipartimento:
            return self._dipartimento

        
