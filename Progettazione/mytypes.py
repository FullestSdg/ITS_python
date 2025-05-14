from enum import *

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

class Voto:

    v:int 

    def __init__(self, v:int):

        if v < 18 or v > 31:
            
            raise ValueError("Il voto v={v} deve essere tra 18 e 31")
        
        self.v = v



print("__name__ all'interno di studente.py " + __name__)

if __name__ == "__main__":

    print("Test di mytypes.py\n==============\n")

    print(Genere.uomo)
    print(type(Genere.uomo))
    print(Genere.donna.upper())
    print(type(Genere.donna.lower()))

    try:
        Genere.donna = 5

    except AttributeError as e:
        print("Non è possibile riassegnare il valore 'donna' del tipo Genere")
        print("\t" + str(e))
    
