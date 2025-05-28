'''
9-13. Dice: Make a class Dice with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
import random

class Dice:

    def __init__ (self, sides:int=6) -> None:

        self.sides = sides

    def roll_dice(self) -> int:

        return f"Il numero uscito è: {random.randint(1, self.sides)}"
    
dado1:Dice = Dice()
dado2:Dice = Dice(20)

for i in range(10+1):
    print(dado1.roll_dice())

print(f"\n=============================================================================")

for i in range(10+1):
    print(dado2.roll_dice())



