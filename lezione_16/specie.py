'''
Specifiche tecniche
1. Classe Specie

- Attributi:
nome (str): Nome della specie.
popolazione (int): Popolazione iniziale.
tasso_crescita (float): Tasso di crescita annuo percentuale.
- Metodi:
__init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
 
2. Sottoclassi BufaloKlingon e Elefante

Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:
Aggiornamento della popolazione per l'anno successivo:
Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
Calcolo della densità di popolazione:
Formula: popolazione / area_kmq
Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
Calcolo degli anni necessari per superare la popolazione di un'altra specie:
Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 
'''


class Specie:

    _nome:str
    _popolazione:int = 0
    _tasso_crescita:float 

    def __init__(self, nome:str, popolazione_iniziale:int, tasso_crescita:float) -> None: 
        
        self._nome = nome 
        self._popolazione = popolazione_iniziale 
        self._tasso_crescita = tasso_crescita

    def cresci(self) -> None:

        popolazione_nuova += self._popolazione * (1 + self._tasso_crescita/100)
        self._popolazione += popolazione_nuova

    def anni_per_superare(self, altra_specie:"Specie",) -> int:
        pass



    def getDensità(self, area_kmq:float) -> int:
        
        densità += self._popolazione / area_kmq
       

class BufaloKlingon(Specie):

    def __init__(self, nome:str, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__(nome, popolazione_iniziale, tasso_crescita)


class Elefante(Specie):

    def __init__(self, nome:str, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__(nome, popolazione_iniziale, tasso_crescita)

