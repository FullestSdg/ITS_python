'''
from typing import Self
from random import randint

class IntGTZ(int):
	def __new__(cls, v:int|float|Self)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be > 0")
		return int.__new__(cls, v)

class NameError(Exception):
    "Nome nonm commpatibile"

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

class Alieno(Creatura):

    __matricola:IntGTZ
    __munizioni:list[IntGTZ]

    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.__matricola = self.setMatricola()
        self.__munizioni = self.setMunizioni()

        if type(nome) != str or nome != "Robot":
            raise NameError("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

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

    def getAssalto(self) -> list[IntGTZ]:
        return self.__assalto

    def setVittoria(self, vittoria:str) -> None:
        
        if type(vittoria) != str:
            self.__urlo_vittoria == "GRAAAHHH"

    def setSconfitta(self, sconfitta:str) -> None:
        
        if type(sconfitta) != str:
            self.__gemito_sconfitta == "Uuurghhh"
    
    def getVittoria(self) -> str:
        return self.__urlo_vittoria

    def getSconfitta(self) -> str:
        return self.__gemito_sconfitta

    def __str__(self):

        nome_alternato = "".join(
            c.lower() if i % 2 == 0 else c.upper()
            for i, c in enumerate(self.__nome)
        )
        return f"Mostro: {nome_alternato}"


class ErrorFight(Exception):

    """ Combattimento non valido """

def pariUguali(a:list[int], b:list[int]) -> list[int]:

    c:list[int] = []
    ultimo_numero_a = a[-1]
    ultimo_numero_b = b[-1]

    if ultimo_numero_a % 2 == 0 and ultimo_numero_b % 2 == 0:

        c.append(1)

    else: 
        c.append(0)

    return c

def combattimento(a:Alieno, m:Mostro) -> Alieno | Mostro | None:

    if not isinstance(a, Alieno) or isinstance(m, Mostro):

        raise ErrorFight(f"{a} non è istanza della classe 'Alieno' oppure {m} non è istanza della classe 'Mostro'")

    else:
        
        c = pariUguali(Alieno.__munizioni, Mostro.__assalto)

        elementi_c = []

        for valori in c:

            if valori == 1:

                elementi_c.append(valori)

            else:
                continue 

        if len(elementi_c) > 4:

            print(Mostro.__urlo_vittoria)
            print(Mostro.__urlo_vittoria)
            print(Mostro.__urlo_vittoria)
            return m

        else:

            print(Mostro.__gemito_sconfitta)
            print(Mostro.__gemito_sconfitta)
            print(Mostro.__gemito_sconfitta)
            return a


def proclamaVincitore(c:Creatura) -> str: 

    for i in range(1,20+1):

        i *= "*"
    print(i)
    print("\n")
    print("*","                 *")
    print("\n")
    print("*  ", Creatura.getNome(c), "  *")
    print("\n")
    print("*","                 *")
    print("\n")
    for i in range(1,20+1):

        i *= "*"
    print(i)

def main():

    alieno = Alieno("Robot")
    mostro = Mostro("Antonio Sbancatore", "FOZZA NAPOLI", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    vincitore = combattimento(alieno, mostro)
    
    print(proclamaVincitore(vincitore))

if __name__ == "__main__":
    main()
'''

from typing import Self
from random import randint

class IntGTZ(int):
	def __new__(cls, v:int|float|Self)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be > 0")
		return int.__new__(cls, v)

class NameError(Exception):
    "Nome nonm commpatibile"

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

class Alieno(Creatura):

    __matricola:IntGTZ
    __munizioni:list[IntGTZ]

    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.setMatricola()
        self.setMunizioni()

        if type(nome) != str or nome != "Robot":
            raise NameError("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

    def setMatricola(self) -> None:
        self.__matricola = IntGTZ(randint(10000, 90000))

    def setMunizioni(self) -> None:
        self.__munizioni = [IntGTZ(x**2) for x in range(0,15+1)]

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
        super().__init__(nome)
        self.__urlo_vittoria = urlo_vittoria
        self.__gemito_sconfitta = gemito_sconfitta
        self.setAssalto()

    def setAssalto(self) -> None:
        lista_numeri:list[IntGTZ] = []
        lista_numeri_duplicati:list[IntGTZ] = []

        for n in range(0,15+1):
            n = IntGTZ(randint(1,100))
            lista_numeri_duplicati.append(n)

            if n not in lista_numeri:   
                lista_numeri.append(n)
        
        self.__assalto = lista_numeri

    def getAssalto(self) -> list[IntGTZ]:
        return self.__assalto

    def setVittoria(self, vittoria:str) -> None:
        if type(vittoria) != str:
            self.__urlo_vittoria = "GRAAAHHH"

    def setSconfitta(self, sconfitta:str) -> None:
        if type(sconfitta) != str:
            self.__gemito_sconfitta = "Uuurghhh"
    
    def getVittoria(self) -> str:
        return self.__urlo_vittoria

    def getSconfitta(self) -> str:
        return self.__gemito_sconfitta

    def __str__(self):
        nome_alternato = "".join(
            c.lower() if i % 2 == 0 else c.upper()
            for i, c in enumerate(self.getNome())
        )
        return f"Mostro: {nome_alternato}"


class ErrorFight(Exception):
    """ Combattimento non valido """

def pariUguali(a:list[int], b:list[int]) -> list[int]:
    c:list[int] = []
    ultimo_numero_a = a[-1]
    ultimo_numero_b = b[-1]

    if ultimo_numero_a % 2 == 0 and ultimo_numero_b % 2 == 0:
        c.append(1)
    else: 
        c.append(0)

    return c

def combattimento(a:Alieno, m:Mostro) -> Alieno | Mostro | None:

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        raise ErrorFight(f"{a} non è istanza della classe 'Alieno' oppure {m} non è istanza della classe 'Mostro'")

    c = pariUguali(a.getMunizioni(), m.getAssalto())

    elementi_c = []

    for valori in c:
        if valori == 1:
            elementi_c.append(valori)

    if len(elementi_c) > 4:
        print(m.getVittoria())
        print(m.getVittoria())
        print(m.getVittoria())
        return m
    else:
        print(m.getSconfitta())
        print(m.getSconfitta())
        print(m.getSconfitta())
        return a


def proclamaVincitore(c:Creatura) -> str: 
    for i in range(1,20+1):
        i *= "*"
    print(i)
    print("\n")
    print("*","                 *")
    print("\n")
    print("*  ", Creatura.getNome(c), "  *")
    print("\n")
    print("*","                 *")
    print("\n")
    for i in range(1,20+1):
        i *= "*"
    print(i)

def main():
    alieno = Alieno("Robot")
    mostro = Mostro("Antonio Sbancatore", "FOZZA NAPOLI", "AAAAAAAAAAAAAAAAAAAAAAAAAA")

    vincitore = combattimento(alieno, mostro)
    
    print(proclamaVincitore(vincitore))

if __name__ == "__main__":
    main()


        






