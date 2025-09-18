from persona import Person 

class Dottore(Person):

    _nome:str 
    _cognome:str 
    _età:int 
    _specializzazione:str 
    _parcella:float 

    def __init__(self, first_name, last_name, specialization:str, parcel:float):
        super().__init__(first_name, last_name)

        if isinstance(specialization, str) and isinstance(parcel, float):

            self._specializzazione = specialization
            self._parcella = parcel 

        elif not isinstance(specialization, str) and not isinstance(parcel, float):

            self._specializzazione = None 
            self._parcella = None 

        elif not isinstance(specialization, str):

            self._specializzazione = None 
            self._parcella = parcel 
            print("La specializzazione inserita non è una stringa")

        elif not isinstance(parcel, float):

            self._parcella = None 
            self._specializzazione = specialization
            print("La parcella inserita non è un float")

    def setSpecialization(self, specialization:str) -> None:

        if isinstance(specialization, str):
            self._specializzazione = specialization

        else:
            print("La specializzazione inserita non è una stringa")

    def setParcel(self, parcel:float) -> None:

        if isinstance(parcel, float):
            self._parcella = parcel

        else:
            print("La parcella inserita non è un float")

    def getSpecialization(self) -> str:
        return self._specializzazione 
    
    def getParcel(self) -> float:
        return self._parcella 
    
    def isAValidDoctor(self) -> bool: 

        if self.getAge() > 30:

            print(f"Doctor: {self._nome} {self._cognome} is valid!")
            return True

        else:
            print(f"Doctor: {self._nome} {self._cognome} is not valid!")
            return False

    def doctorGreet(self) -> None:

        if self.isAValidDoctor() == True:  
            print(self.greet() + f"\nSono un medico {self.getSpecialization()}")

    

# GiuseppeRoberto = Person("Giuseppe", "Roberto")
# GiuseppeRoberto.setAge(21)
# print(GiuseppeRoberto.getAge())

# DottorGiuseppe = Dottore("Giuseppe", "Roberto", "Infermiere", 1214)
# print(DottorGiuseppe.getSpecialization())
# print(DottorGiuseppe.getParcel())
# print(DottorGiuseppe.getName())
# print(DottorGiuseppe.getLastName())

# DottorGiuseppe.setAge(31)

# DottorGiuseppe.isAValidDoctor()
# DottorGiuseppe.doctorGreet()

# DottorGiuseppe.setAge(29)
# DottorGiuseppe.doctorGreet() # Chiedere perchè stampa comunque is not valid 
