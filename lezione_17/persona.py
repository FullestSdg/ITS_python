class Person:

    _nome:str 
    _cognome:str 
    _età:int 

    def __init__(self, first_name:str, last_name:str) -> None:

        if isinstance(first_name, str) and isinstance (last_name, str):

            self._nome = first_name 
            self._cognome = last_name 
            self._età = 0
        
        elif not isinstance(first_name, str) and not isinstance(last_name, str):
        
            self._nome = None 
            self._cognome = None
            self._età = None 
            
        elif not isinstance(first_name, str):

            self._cognome = last_name
            self._nome = None 
            print("Il nome inserito non è una stringa!")

        elif not isinstance(last_name, str):

            self._nome = first_name
            self._cognome = None
            print("Il cognome inserito non è una stringa!")

    def setName(self, first_name:str) -> None:

        if isinstance(first_name, str):

            self._nome = first_name 

        else:
            print("Il nome inserito non è una stringa")
    
    def setLastName(self, last_name:str) -> None:

        if isinstance(last_name, str):

            self._cognome = last_name 

        else:
            print("Il cognome inserito non è una stringa")

    def setAge(self, age:int) -> None:
        
        if isinstance(age, int):

            self._età = age  

        else:
            print("L'età inserita non è un numero intero")
    
    def getName(self) -> str:
        return self._nome
    
    def getLastName(self) -> str:
        return self._cognome 
    
    def getAge(self) -> int:
        return self._età 
    
    def greet(self) -> None:

        print(f"Ciao, sono {self._nome} {self._cognome}!"+\
              f"\nHo {self._età} anni!")



GiuseppeRoberto = Person("Giuseppe", "Roberto")
# print(GiuseppeRoberto.getName())
# print(GiuseppeRoberto.getLastName())

# GiuseppeRoberto.setAge(21)

# print(GiuseppeRoberto.getAge())
# GiuseppeRoberto.greet()

DanielErcoli = Person("Daniel", 973)
# print(DanielErcoli.getName())
# print(DanielErcoli.getLastName())

ValerioBonaventura = Person(32,35)
# print(ValerioBonaventura.getName())
# print(ValerioBonaventura.getLastName())
# print(ValerioBonaventura.getAge())
