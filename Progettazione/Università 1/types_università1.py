from typing import Self
import re

class Voto:

	def __init__(self, v:int):
		if v < 18 or v > 30:
			raise ValueError(f"Value v must be between 18 and 31, now {v}")
		self._value = v

	def valore(self)->int:
		return self._value

	def __hash__(self)->int:
		return hash(self.valore())
	
	def __eq__(self, other)->bool:
		if other is None:
			return False

		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				return False

		assert type(other) == type(self)
		
		if hash(self) != hash(other):
			return False
		else:
			return self.valore() == other.valore()

	def __lt__(self, other)->bool:
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between Voto and {type(other)}")
		return self.valore() < other.valore()

	def __gt__(self, other):
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between Voto and {type(other)}")
		return self.valore() > other.valore()

	def __repr__(self)->str:
		return repr(self.valore())
	

#----------------------------------------------------------------------------------------------------------------------------

class IntGT1900(int):
	
	def __new__(cls, v:int|float|Self)->Self:
		
		if v < 1900:	
			raise ValueError(f"Value v == {v} must be >= 1900")
		
		return int.__new__(cls, v)


#----------------------------------------------------------------------------------------------------------------------------

class RealGTZ(float):

    def __new__(cls, v: int | float | str | bool | Self) -> Self:

        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")

#----------------------------------------------------------------------------------------------------------------------------

class CodiceFiscale:
    def _init_(self, codice):
        if not self._valida_codice(codice):
            raise ValueError("Codice Fiscale non valido.")
        self.codice = codice.upper()

    def _str_(self):
        return self.codice

    def _eq_(self, other):
        if isinstance(other, CodiceFiscale):
            return self.codice == other.codice
        return False

    def _len_(self):
        return len(self.codice)

    @staticmethod
    def _valida_codice(codice):
        # Un codice fiscale valido è lungo 16 caratteri e segue un pattern specifico
        pattern = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        return bool(re.match(pattern, codice.upper()))

    def is_valid(self):
        return self._valida_codice(self.codice)
	
#----------------------------------------------------------------------------------------------------------------------------