from impiegato import Impiegato
from progetto import Progetto 
from datetime import date
from progetto import Progetto


class Coinvolto:

    class _link:

        _impiegato:Impiegato # noto alla nascita
        _progetto:Progetto # noto alla nascita
        _data_afferenza:date # noto alla nascita << immutabile >>

        def __init__(self, impiegato:Impiegato, progetto:Progetto, data_afferenza:date) -> None:

            self._impiegato = impiegato 
            self._progetto = progetto 
            self._data_afferenza = data_afferenza

        def impiegato(self) -> Impiegato:
            return self._impiegato 
        
        def progetto(self) -> Progetto:
            return self._progetto
        
        def data_afferenza(self) -> date:
            return self._data_afferenza

        

        