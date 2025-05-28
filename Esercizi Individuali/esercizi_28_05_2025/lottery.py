'''
9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

'''
import random

from typing import Any


class LotteryMachine:

    def __init__(self, vincita:list[Any]=[1,2,3,4,5,6,7,8,9,0,"h","c","a","o"]) -> None:

        self.vincita = vincita

    def random_selection(self, biglietto_vincente:str = None) -> None:

        self.biglietto_vincente = random.randint(4,self.vincita)

    def winning_message(self) -> str:

        return f"Se il vostro biglietto è {self.biglietto_vincente}!\nCongratulazioni avete vinto!!!! "


lottery:LotteryMachine = LotteryMachine()
print(lottery.random_selection())



