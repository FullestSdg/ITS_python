class Persona:

    def __init__(self, name:str, last_name:str, age:int ):

        self.name = name
        self.last_name = last_name
        self.age = age
    
    # funzione della classe Persona che visualizza in output i dati di una persona

    def displayData(self) -> None:

        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")
