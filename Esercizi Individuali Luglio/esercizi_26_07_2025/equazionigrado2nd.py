'''
Write a Python program to solve quadratic equation.

The standard form of a quadratic equation is 
		
			ax2 +bx + c = 0

where 
a,b and c are real numbers and a =! 0

The solutions of this quadratic equation is given by:

(-b +- (b2 -4ac)1/2)/(2a)
'''
from math import *
from typing import *



class AX2:

    _sign:str 
    _number:float

    def __init__(self, sign:str, number:float) -> None:

        self.setSign(sign)
        self.setNumber(number)

    def setSign(self, sign:str) -> None:

        if sign not in ("+", "-"):
            raise ValueError("Devi inserire un segno '+' o '-'")

        else:
            self._sign = sign

    def setNumber(self, number:float) -> None:

        if number == 0:
            raise ValueError("Il valore di 'a' non può essere 0")

        else:
            self._number = number

    def getSign(self) -> str:
        return self._sign 
    
    def getNumber(self) -> float: 
        return self._number
    
    def getEffectiveValue(self) -> float:
        return self._number if self._sign == "+" else -self._number




class BX:

    _sign:str 
    _number:float

    def __init__(self, sign:str, number:float) -> None:

        self.setSign(sign)
        self.setNumber(number)

    def setSign(self, sign:str) -> None:

        if sign not in ("+", "-"):
            raise ValueError("Devi inserire un segno '+' o '-'")

        else:
            self._sign = sign

    def setNumber(self, number:float) -> None:
        self._number = number

    def getSign(self) -> str:
        return self._sign 
    
    def getNumber(self) -> float: 
        return self._number

    def getEffectiveValue(self) -> float:
        return self._number if self._sign == "+" else -self._number

class C: 

    _sign:str 
    _number:float

    def __init__(self, sign:str, number:float) -> None:

        self.setSign(sign)
        self.setNumber(number)

    def setSign(self, sign:str) -> None:

        if sign not in ("+", "-"):
            raise ValueError("Devi inserire un segno '+' o '-'")

        else:
            self._sign = sign

    def setNumber(self, number:float) -> None:
        self._number = number

    def getSign(self) -> str:
        return self._sign 
    
    def getNumber(self) -> float: 
        return self._number
    
    def getEffectiveValue(self) -> float:
        return self._number if self._sign == "+" else -self._number



class NoPositiveOrNegative(Exception):
    "Manca il segno '+' o '-'"



class SecondGradeEquation:

    _ax2:AX2
    _bx:BX
    _c:C

    def __init__(self, ax2:AX2, bx:BX, c:C) -> None:

        self.setAX2Value(ax2)
        self.setBXValue(bx)
        self.setCValue(c)

    def setAX2Value(self, ax2:AX2) -> None:

        if ax2 != 0 and ax2.getSign() in ("+", "-"):
            self._ax2 = ax2

        elif ax2 == 0:
            self._ax2 = 1 

        else:
            raise NoPositiveOrNegative("Il tuo valore manca di segno positivo ('+') o negativo ('-')!")

    def setBXValue(self, bx:BX) -> None:

        if bx.getSign() in ("+", "-"):
            self._bx = bx

        else:
            raise NoPositiveOrNegative("Il tuo valore manca di segno positivo ('+') o negativo ('-')!")

    def setCValue(self, c:C) -> None: 

        if c.getSign() in ("+", "-"):
            self._c = c

        else:
            raise NoPositiveOrNegative("Il tuo valore manca di segno positivo ('+') o negativo ('-')!")

    def getAX2Value(self) -> str:
        return f"{self._ax2.getSign()}{self._ax2.getNumber()}x²"
    
    def getBXValue(self) -> str:
        return f"{self._bx.getSign()}{self._bx.getNumber()}x"

    def getCValue(self) -> float:
        return f"{self._c.getSign()}{self._c.getNumber()}"
    
    def __str__(self) -> str:
        return f"{self.getAX2Value()} {self.getBXValue()} {self.getCValue()} = 0"



def SecondGradeEquationSolver(equation:SecondGradeEquation) -> str:

    a = equation._ax2.getEffectiveValue()
    b = equation._bx.getEffectiveValue()
    c = equation._c.getEffectiveValue()

    if a == 0:
        raise ValueError("Il valore 'a' di un'equazione di secondo grado non può essere uguale a 0")
    
    delta = b**2 - 4*a*c

    if delta < 0:
        return "L'equazione non ha soluzioni reali."
    
    elif delta == 0:

        x = -b / (2*a)
        return f"L'equazione ha una soluzione doppia: x = {x}"
    
    else:

        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return f"Il valore di x₁ è +/-: {round(x1, 2)}\nIl valore di x₂ è +/-: {round(x2, 2)}"