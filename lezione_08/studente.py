from persona import Persona

class Studente(Persona):

    '''
    Attributi della classe Persona:
    self.name:str
    self.last_name:str
    self.age:int

    Attributi della classe Studente:
    self.mnatricola:str
    '''

    #Inizializzo un oggetto della classe studente

    def __init__(self, name:str, last_name:str, age:int, matricola:str):
        #Inizializzo una classe Persona chiamando un metodo __init__ della superclasse
        super().__init__(name, last_name, age)

        #Istruzioni che inizializzano un oggetto della classe Studente
        self.setMatricola(matricola)

    #metodi setter:

    def setMatricola(self,matricola:str) -> None:

        if matricola:
            
            self.matricola = matricola
        
        else:
            print("Errore! La matricola non può essere rappresentata da una stringa vuota!")

    #metodi getter:

    #metodo che ritorna il valore dell'attributo self.matricola

    def getMatricola(self) -> str:

        return self.matricola
    
    #ridefinire il metodo __str__ (overriding)

    def __str__(self) -> str:
        
        return f"\nNome: {self.name}\nCognome: {self.getLastName()}\nEtà: {self.getAge()}\nMatricola: {self.getMatricola()}"