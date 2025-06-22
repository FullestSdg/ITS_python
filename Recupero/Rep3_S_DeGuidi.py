from typing import Self
from random import randint

class IntGTZ(int):
	def __new__(cls, v:int|float|Self)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be > 0")
		return int.__new__(cls, v)

class NameError(Exception):

    "Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!"   

class Creatura:

    __nome:str

    def __init__(self, nome:str) -> None:
        self.__nome = nome 

    def setNome(self, new_nome:str) -> None:

        if type(new_nome) != str:
            self.__nome = "Creatura Generica"
        
        elif len(new_nome) == 0:
            self.__nome = "Creatura Generica"

        else:
            self.__nome = new_nome

    def getNome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.__nome}"


creatura:Creatura = Creatura("Totti")
print(creatura)

creatura.setNome("")
print(creatura.getNome())
print(creatura)

class Alieno(Creatura):

    __matricola:IntGTZ
    __munizioni:list[IntGTZ]

    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.__matricola = self.setMatricola()
        self.__munizioni = self.setMunizioni()

        if type(nome) != str and nome != "Robot":
            raise NameError

    def setMatricola(self) -> None:
        self.__matricola = randint(10000, 90000)

    def setMunizioni(self) -> None:
        self.__munizioni = [x**2 for x in range(0,15+1)]

    def getMatricola(self) -> IntGTZ:
        return self.__matricola
    
    def getMunizioni(self) -> list[IntGTZ]:
        return self.__munizioni
    
    def getNome(self) -> str:
        return f"{super().getNome()}"
    
    def __str__(self) -> str:
        return f"Alieno: {self.getNome()}-{self.__matricola}"
    
class Mostro(Creatura):
     
    __urlo_vittoria:str
    __gemito_sconfitta:str
    __assalto:list[IntGTZ]

    def __init__(self, nome:str, urlo_vittoria:str, gemito_sconfitta:str) -> None:
         
        self.__nome = nome 
        self.__urlo_vittoria = urlo_vittoria
        self.__gemito_sconfitta = gemito_sconfitta
        self.__assalto = self.setAssalto()

    def setAssalto(self) -> None:
        lista_numeri:list[IntGTZ] = []
        lista_numeri_duplicati:list[IntGTZ] = []

        for n in range(0,15+1):

            n = randint(1,100)
            lista_numeri_duplicati.append(n)

            if n not in lista_numeri:   
                lista_numeri.append(n)
        
        self.__assalto = lista_numeri


alieno: Alieno = Alieno("Robot")
alieno.setMatricola()

print(alieno)