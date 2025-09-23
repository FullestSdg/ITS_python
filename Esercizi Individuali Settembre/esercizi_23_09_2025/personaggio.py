from random import *

class Character:

    _nome:str
    _livello:int 
    _hp:int 
    _attacco:int 
    _difesa:int
    _mana:int

    def __init__(self, nome:str) -> None:

        if isinstance(nome, str):

            self._nome = nome
            self.setLevel()
            self.setHP()
            self.setAttacco()
            self.setDifesa() 
            self.setMana()

        else:            
            self._nome = None
            self._livello = None
            self._hp = None
            self._attacco = None
            self._difesa = None 
            self._mana = None
            print(f"Il nome del tuo personaggio deve essere una stringa")
    
    def setName(self, new_name:str) -> None:
        
        if isinstance(new_name, str):
            self._nome = new_name
        
        else:
            print(f"Il nome del tuo personaggio deve essere una stringa")

    def setLevel(self) -> None:
        self._livello = randint(1,50)

    def setHP(self) -> None:
        self._hp = randint(1000,5000)
    
    def setAttacco(self) -> None:
        self._attacco = randint(50,150)
    
    def setDifesa(self) -> None:
        self._difesa = randint(25,100)
    
    def setMana(self) -> None:
        self._mana = randint(200,500)
    
    def getName(self) -> str:
        return self._nome

    def getLevel(self) -> int:
        return self._livello
    
    def getHP(self) -> int:
        return self._hp 
    
    def getAttacco(self) -> int:
        return self._attacco 
    
    def getDifesa(self) -> int:
        return self._difesa 
    
    def getMana(self) -> int:
        return self._mana
    
    def isAlive(self) -> bool:

        if self._hp > 0:
            return True 
        
        else:
            return False
    
    def getDamage(self, danno:int) -> None:
        self._hp -= danno

    def info(self) -> str:
        return f"Stats Character: {self._nome}\nLevel: {self._livello}\nHP: {self._hp}\nAttackDamage: {self._attacco}\nDefense: {self._difesa}\nMana: {self._mana}"





