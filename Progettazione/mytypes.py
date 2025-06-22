from enum import *
from typing import Self
import re
from datetime import *
from typing import Any

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



class IntGTZ(int):
	def __new__(cls, v:int|float|Self)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be > 0")
		return int.__new__(cls, v)



class Voto(int):
	def __new__(cls, v:int|Self)->Self:
		if v < 18 or v > 30:
			raise ValueError(f"Value v == {v} must be between 18 and 30")
		return int.__new__(cls, v)
      



class Telefono(str):
	def __new__(cls, t:str|Self)->Self:
		if not re.fullmatch('\+?[0-9]+', t):
			raise ValueError(f"Value t == {t} does not comply to standard")
		return str.__new__(cls, t)
	


class TimeRange(tuple):	
	_start: datetime|None # [0..1]
	_end: datetime|None # [0..1]
	# subject to constraint: _start <= _end

	def __new__(cls, start:datetime|str|None, end:datetime|str|None)->Self:	
		# We accept _start == None or _end == None (unbounded time periods)

		values = [ datetime.fromisoformat(x) if isinstance(x, str) else x for x in [start, end] ]
		if values[0] and values[1] and values[0] > values[1]:
			raise ValueError(f"Invalid TimeRange(from={start}, to={end}): 'from' must be <= 'to'")
		return tuple.__new__(cls, values)

	def start(self)->datetime|None:
		return self[0]
	def end(self)->datetime|None:
		return self[1]

	def duration(self)->timedelta|None:
		try:
			return self.end() - self.start()
		except:
			return timedelta.max # we should return timedelta(+infty), but timedelta has no standard representation of +infty

	def is_disjoint(self, other:Self)->bool:

		# case #1:
		# self :        X---------------
		# other: ---X           

		# case #2:
		# self : ---------------X
		# other:                   X----

		# case #3:
		# self :        X-------X
		# other: ---X      or      X----

		if self.start(): #1, #3
			if other.end() and other.end() < self.start():
				return True #1
			
		if self.end(): #2, #3
			if other.start() and other.start() > self.end():
				return True #3

		return False

	def intersects(self, other:Self)->bool:
		return not self.is_disjoint(other)

	def shift(self, delta:timedelta)->Self:
		if not delta:
			return self
		else:
			return TimeRange(
				None if not self.start() else self.start() + delta, 
				None if not self.end() else self.end() + delta)

	def __str__(self)->str:
		return f"{ f'[{self[0]}' if self[0] else '(-infinity'}, { f'{self[1]}]' if self[1] else '+infinity)'}"



class Indirizzo:
	# campi dati:
	# _via:str
	# _civico:...
	def __init__(self, via:str, civico:str):
		if via is None:
			raise ValueError(f"via cannot be None")
		if civico is None:
			raise ValueError(f"civ cannot be None")
		
		self._via:str = via

		if not re.search("^[0-9]+[a-zA-Z]*$", civico):
			raise ValueError(f"value for civico '{civico}' not allowed")
		self._civico:str = civico
	
	def via(self)->str:
		return self._via
	def civico(self)->str:
		return self._civico

	def __repr__(self)->str:
		return f"Indirizzo(via={self.via()}, civico={self.civico()})"


	# class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
	def __hash__(self)->int:
		return hash( (self.via(), self.civico()) )

	def __eq__(self, other:Any)->bool:
		if other is None or \
				not isinstance(other, type(self)) or \
				hash(self) != hash(other):
			return False
		return (self.via(), self.civico() ) == (other.via(), other.civico())
	
