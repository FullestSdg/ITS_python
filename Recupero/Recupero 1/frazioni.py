class Frazione:

    _numeratore:int 
    _denominatore:int 

    def __init__(self, numeratore:int, denominatore:int) -> None:

        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)
    
    def setNumeratore(self, numeratore_nuovo) -> None: 
        
        if type(numeratore_nuovo) != int:
        
            self._numeratore = 13
        
        else:
            self._numeratore = numeratore_nuovo

    def setDenominatore(self, denominatore_nuovo) -> None:
        
        if type(denominatore_nuovo) != int or denominatore_nuovo == 0:

            self._denominatore = 5
        
        else:
            self._denominatore = denominatore_nuovo

    def getNumeratore(self) -> int: 
        return self._numeratore

    def getDenonminatore(self) -> int: 
        return self._denominatore

    def __str__(self) -> str: 
        return f"{self._numeratore}/{self._denominatore}" 

    def value(self) -> float:
        return f"{(self._numeratore / self._denominatore):.3f}"

def mcd(x:int, y:int) -> int:
    
    lista_divisibili_x:list[int] = []
    lista_divisibili_y:list[int] = []

    for i in range(1,x+1):

        if x % i == 0:
            lista_divisibili_x.append(i)
    
    for i in range(1,y+1):

        if y % i == 0:
            lista_divisibili_y.append(i)

    return max(set(lista_divisibili_x) & set(lista_divisibili_y))

    

print(mcd(3,6))





