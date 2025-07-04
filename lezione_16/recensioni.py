class Media:

    _title:str
    _reviews:list[int]

    def __init__(self, titolo:str, reviews:list[int]) -> None:

        self._title = titolo 
        self._reviews = reviews 

        for i in self._reviews:

            if i < 0 or i > 5:

                raise ValueError("Numero inserito non valido")
        
    def set_title(self, title:str) -> None:
        self._title = title 
    
    def get_title(self) -> str:
        return self._title
    
    def aggiungiValutazione(self, voto:int) -> None:

        if voto < 0 or voto > 5:
            raise ValueError("NUmero inserito non valido")
        
        else:
            self._reviews.append(voto)
    
    def getMedia(self) -> int | float:

        somma_lista = 0

        for voti in self._reviews:

            somma_lista += voti

        self.media = somma_lista / len(self._reviews)

        return self.media 
    
    def getRate(self) -> str:

        match self.media:

            case self.media if self.media <= 1.5:
                return "Terribile"
            
            case self.media if self.media <= 2.5:
                return "Brutto"
            
            case self.media if self.media <= 3.5:
                return "Normale"
            
            case self.media if self.media <= 4.5:
                return "Bello"
            
            case _:
                return "Grandioso"

    def ratePercentage(self, voto:int) -> str:
        
        lista_voti:list[int] = []

        for voti in self._reviews:

            if voto == voti:

                lista_voti.append(voti)
            
            else:
                continue

        percentuale = (len(lista_voti) / len(self._reviews)) * 100

        return f"{percentuale}%"
    
    def recensione(self) -> str:

        return f"Titolo del Film: {self._title}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}\nBrutto: {self.ratePercentage(2)}\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}\nGrandioso: {self.ratePercentage(5)}"

class Film(Media):

    def __init__(self, titolo:str) -> None:
       super().__init__(titolo)

        
media = Media("ER PUPO", [4,3,5,4,3,3,5,2,3,4])

print(media.getMedia())
print(media.getRate())
print(media.ratePercentage(5))
print("\n")
print(media.recensione())

# print(film.getRate())