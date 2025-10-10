
class Specifiche:

    _specifiche:list[str]

    def __init__(self) -> None:
        self._specifiche = []


class Ricette:

    _ricette:list[str]
    
    def __init__(self) -> None:

        self._ricette = []

    def aggiungiRicetta(self, ricetta:str) -> None:

        if ricetta not in self._ricette:
            self._ricette.append(ricetta)
    
    def rimuoviRicetta(self, ricetta:str) -> None:

        if ricetta in self._ricette:
            self._ricette.remove(ricetta)
    
    def cercaRicetta(self, ricetta:str) -> str | None:

        if ricetta in self._ricette:

            for r in self._ricette:

                if r == ricetta:
                    return ricetta
                
        else:
            return None
        
    def cheRicettaHoMangiato(self):
        pass