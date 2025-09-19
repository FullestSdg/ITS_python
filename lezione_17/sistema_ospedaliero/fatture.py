from paziente import Paziente 
from dottore import Dottore

class Fattura:

    _dottore:Dottore 
    _patient:list[Paziente] = []
    _fatture:int
    _salary:int

    def __init__(self, patient:list[Paziente], doctor:Dottore) -> None: 

        if doctor.isAValidDoctor() == True:
            self._patient = patient 
            self._dottore = doctor
            self._fatture = len(patient)
            self._salary = 0
        
        else:
            self._dottore = None 
            self._patient = None 
            self._fatture = None 
            self._salary = None 
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self) -> int:
        
        if self._patient is not None:
            self._fatture = len(self._patient)
            
        else:
            self._fatture = 0

        if self._dottore is not None:
            return self._dottore.getParcel() * self._fatture
        
        else:
            return 0
    
    def getFatture(self) -> int: 
        
        self._fatture = len(self._patient)
        return self._fatture

    def addPatient(self, newPatient:Paziente) -> None:

        if newPatient not in self._patient:

            self._patient.append(newPatient)

            self._fatture = self.getFatture()
            self._salary = self.getSalary()

            print(f"Alla lista del Dottor {self._dottore.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        
        else:
            print(f"Paziente già nella lista del Dottor {self._dottore.getLastName()} ")

    def removePatient(self, idCode:str) -> None:

        for paziente in self._patient:

            if paziente.getIdCode() == idCode: 

                self._patient.remove(paziente)

                self._fatture = self.getFatture()
                self._salary = self.getSalary()

                print(f"Alla lista del Dottor {self._dottore.getLastName()} è stato rimosso il paziente {idCode}")

            else:
                print(f"Non esiste nessun paziente con ID: {idCode} nella lista del Dottor {self._dottore.getLastName()}")

