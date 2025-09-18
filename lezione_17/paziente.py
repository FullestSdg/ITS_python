from persona import Person

class Paziente(Person):

    _nome:str 
    _cognome:str 
    _età:int
    _codice_identificativo:str 

    def __init__(self, first_name:str, last_name:str, codice_identificativo:str):
        super().__init__(first_name, last_name)

        if isinstance(codice_identificativo, str):

            self._codice_identificativo = codice_identificativo

        else:
            print("Il codice identificativo inserito non è una stringa!")
    
    def setIdCode(self, idCode:str) -> None:

        if isinstance(idCode, str):

            self._codice_identificativo = idCode
        
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def getIdCode(self) -> str:
        return self._codice_identificativo
    
    def patientInfo(self) -> None:

        print(f"Paziente: {self.getName()} {self.getLastName()}" +\
         f"\nID: {self._codice_identificativo}")


# paziente = Paziente("Francesco", "Totti", "129573")

# print(paziente.getAge())
# print(paziente.getName())
# print(paziente.getLastName())

# print(paziente.getIdCode())
# paziente.patientInfo()
