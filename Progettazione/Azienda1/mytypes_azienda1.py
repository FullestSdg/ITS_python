from typing import Self
import re
from typing import Any

class RealGEZ(float):

    def __new__(cls, number:float| int | bool | str | Self) -> Self:

        if number >= 0:
        
            return number
        
        else:
            raise ValueError(f"Il numero inserito {number} deve essere maggiore di 0 e un reale")
        

class CAP(str):
    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^\d{5}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")

class Indirizzo:
    # campi dati:
    _via:str
    _civico: str
    _cap: CAP
    def __init__(self, via: str, civico: str, cap: CAP) -> None:
        self._via: str = via

        if not re.search("^[0-9]+[a-zA-Z]*$", civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico: str = civico
        self._cap: CAP = cap

    def via(self) -> str:
        return self._via

    def civico(self) -> str:
        return self._civico

    def cap(self) -> str:
        return self._cap

    def __repr__(self) -> str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()}, cap={self.cap()})"

    def __str__(self) -> str:
        return f"{self.via()} {self.civico()} - {self.cap()}"

    # class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
    def __hash__(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())

class Telefono(str):
	def __new__(cls, t:str|Self)->Self:
		if not re.fullmatch(r'\+?[0-9]+', t):
			raise ValueError(f"Value t == {t} does not comply to standard")
		return str.__new__(cls, t)





    