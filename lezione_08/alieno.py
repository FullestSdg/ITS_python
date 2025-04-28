class Alieno:
    '''
    di un alieno ci interessa sapere la
    galassia di provenienza
    self.galaxy:str
    '''

    #inizializzare un oggetto della classe Alieno
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str) -> None:

        if galaxy:
            self.galaxy = galaxy 
        
        else:
            print("Errore! La stringa è vuota!")
    
    def getGalaxy(self) -> str:

        return self.galaxy
    
    def speak(self) -> None:

        print("\nsdfbhasdhfd!\n")

    def __str__(self) -> str:

        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}!\n"
