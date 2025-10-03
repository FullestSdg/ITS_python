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
        self._hp = 500 + (self._livello * 100)
    
    def setAttacco(self) -> None:
        self._attacco = 20 + (self._livello * 3)
    
    def setDifesa(self) -> None:
        self._difesa = 10 + (self._livello * 2)
    
    def setMana(self) -> None:
        self._mana = 100 + (self._livello * 5)
    
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





