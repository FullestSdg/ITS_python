from impiegato import Impiegato
from dipartimento import Dipartimento
from progetto import Progetto 
from datetime import date
from dipartimento import Dipartimento

class Afferenza:

    _impiegato:Impiegato # noto alla nascita
    _dipartimento:Dipartimento # noto alla nascita
    _data_afferenza:date # non noto alla nascita << immutabile >>

    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, _data_afferenza:date) -> None:

        self._data_afferenza = _data_afferenza
        self._impiegato = impiegato
        self._dipartimento = dipartimento

    def setImpiegato(self, impiegato:Impiegato) -> None:
        self._impiegato = impiegato
    
    def setDipartimento(self, dipartimento:Dipartimento) -> None:
        self._dipartimento = dipartimento

    def getImpiegato(self) -> Impiegato:
        return self._impiegato
    
    def getDipartimento(self) -> Dipartimento:
        return self._dipartimento

    def data_afferenza(self) -> date:
        return self._data_afferenza

