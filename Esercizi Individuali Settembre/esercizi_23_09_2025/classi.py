from personaggio import *
import random 
from random import *

class Warrior(Character):

    # La classe "Warrior" ha:
    # Attacco +15%
    '''_ability_buff_active:bool = False'''
    _cooldown:int = 0

    def __init__(self, nome):
        super().__init__(nome)

        self._attacco += int((self._attacco * 15) / 100)

        '''self._buff_turns_left = 0
        self._original_stats = {}'''
    '''
    def requirementsSpecialAbility(self) -> bool:

        if self._livello >= 30 and self._mana >= 100 and not self._ability_buff_active and self._cooldown == 0: # chiedere perchè not invece che == True

            self.activateSpecialAbility()
            return True
        
        else:
            return False

    def activateSpecialAbility(self) -> None:

        print(f"!! Berserk Mode Activated !!\nNew AttackDamage = {self._attacco} + 15%\nNew HealthPoints = {self._hp} + 10%")
        
        self._original_stats["hp"] = self._hp 
        self._original_stats["attacco"] = self._attacco

        self._hp += int((self._hp * 10) / 100)
        self._attacco += int((self._attacco * 15) / 100)
                
        self._mana -= 50

        self._ability_buff_active = True
        self._buff_turns_left = 3
        self._cooldown = 2

    def onTurnEnd(self) -> None: 
        # Va chiamato a fine turno


        if self._ability_buff_active:
            self._buff_turns_left -= 1 

            if self._buff_turns_left <= 0:
                self.deactivateSpecialAbility()
                self._cooldown = 2 # da vedere 

    def deactivateSpecialAbility(self) -> None:

        print(">> Berserk Mode Ended <<")

        self._hp = self._original_stats["hp"]
        self._attacco = self._original_stats["attacco"]

        self._ability_buff_active = False 
        self._original_stats = {}'''

class Tank(Character):

    # La classe "Tank" ha:
    # Difesa +35% 
    # Hp +15% 
    # Attacco -20% 

    def __init__(self, nome):
        super().__init__(nome)

        self._difesa += int((self._difesa * 35) / 100)
        self._hp += int((self._hp * 15) / 100)
        self._attacco -= int((self._attacco * 20) / 100) 

class Assassin(Character):

    # La classe "Assassin" ha:
    # Attacco +40%
    # Hp -20% 
    # Difesa -20%

    def __init__(self, nome):
        super().__init__(nome)

        self._attacco += int((self._attacco * 40) / 100) 
        self._difesa -= int((self._difesa * 20) / 100)
        self._hp -= int((self._hp * 20) / 100)


class Mage(Character):
    
    # La classe "Mage" ha 2 sottoclassi, tuttavia hanno deei bonus statistiche predefiniti all'interno di questa:
    # Healer & SpellCaster 
    # Mana +70%
    # Attacco -15%
    # Difesa -15% 
    # Hp -10%

    def __init__(self, nome):
        super().__init__(nome)

        self._attacco -= int((self._attacco * 15) / 100) 
        self._difesa -= int((self._difesa * 15) / 100)
        self._hp -= int((self._hp * 10) / 100)
        self._mana += int((self._mana * 70) / 100)

class Healer(Mage):

    _cooldown:int = 0
    
    def __init__(self, nome):
        super().__init__(nome)

    def requirementsSpecialAbility(self) -> bool:

        if self._livello >= 30 and self._mana >= 400 and self._cooldown == 0:

            self.activateSpecialAbility()
        
        else:
            print(f"Livello dell'healer troppo basso per eseguire la sua abilità speciale!")

    def activateSpecialAbility(self, alleati:list[Character]) -> None:

        print(f"!! Healing Enchantment Activated !!\nHealing = 100 + {int(self._livello * 2.45)}")
        
        for character in alleati: 
            character.setHP() += 100 + {int(self._livello * 2.45)}
            
        self._mana -= 400
        self._cooldown = 2

    def onTurnEnd(self) -> None: 
        # Va chiamato a fine turno  
        self._cooldown -= 1

class SpellCaster(Mage):

    _ability_buff_active:bool = False
    _cooldown = 0
    _abilities:list[function]
    
    def __init__(self, nome):
        super().__init__(nome)

        self._abilities = [self.__fireballSpecialAbility(), self.__empoweringSpecialAbility, self.__debuffingSpecialAbility()]
        self._avversari = []
        self._alleati = []

    def activateSpecialAbility(self, avversari:list[Character], alleati:list[Character]) -> None:

        self._avversari = avversari 
        self._alleati = alleati 

        effetto = random.sample(self._abilities, 1)[0]

    def __fireballSpecialAbility(self) -> None:

        if self._livello >= 30 and self._mana >= 100 and not self._ability_buff_active and self._cooldown == 0:
 
            pass
        
        



    def __empoweringSpecialAbility(self) -> None:
        pass 

    def __debuffingSpecialAbility(self) -> None:
        pass

