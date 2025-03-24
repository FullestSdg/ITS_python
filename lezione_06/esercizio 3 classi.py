class Animal:

    def __init__(self,name:str, legs:int = None):
        self.name = name
        self.legs = legs
    
    def setLegs(self,legs:int):
        self.legs = legs

    def getLegs(self,get_legs:int):        
        return get_legs
    
    def printInfo(self, name:str,legs:int):

        print(f"{self.name}\n {self.legs}")
        
animale = Animal("Giraffa", 4)
print(animale)
    

animale2 = Animal("Squalo", 0)
print(animale2)


