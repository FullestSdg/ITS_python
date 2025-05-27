from typing import Self
import re

class GTZ(float):

    def __new__(cls, number:float| int | bool | str | Self) -> Self:

        if number >= 0:
        
            return number
        
        else:
            raise ValueError(f"Il numero inserito {number} deve essere maggiore di 0 e un reale")
        

class Indirizzo:

    def __init__(self, via:str, civico:str):

        self.via = via
        self.civico = civico

    def get_via(self) -> str:

        return self.via
    
    def get_civico(self) -> str:

        return self.civico
    
class Telefono(str):

    def __new__(cls, telephone_number:str):

        if re.fullmatch((r"(?:\+39|0039)\d{10}")):

            return str.__new__(cls, telephone_number)
        
        else:
            raise ValueError(f"Il numero di telefono inserito {telephone_number} non è valido in Italia")





    