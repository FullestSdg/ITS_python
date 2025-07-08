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


def semplifica(l:list[Frazione]) -> list[Frazione]:

    lista_frazioni_irriducibili:list[Frazione] = []

    for i in l:

        if mcd(i.getNumeratore(), i.getDenonminatore()) == 1:
            lista_frazioni_irriducibili.append(i)
        
        else:
              
            denominatore_semplificato = int(i.getDenonminatore() / mcd(i.getNumeratore(), i.getDenonminatore()))
            numeratore_semplificato = int(i.getNumeratore() / mcd(i.getNumeratore(), i.getDenonminatore()))

            frazione = Frazione(numeratore_semplificato, denominatore_semplificato)

            lista_frazioni_irriducibili.append(frazione)
    
    return lista_frazioni_irriducibili


def fractionCompare(l:list[Frazione], f:list[Frazione]) -> float:

    i = 0
    while i < len(l):

        originale = float(l[i].value())
        semlificato = float(f[i].value())

        print(f"Valore frazione originale: {originale:.3f} --- Valore frazione ridotta: {semlificato:.3f}")
    
        i += 1
    
    return ""

l = [Frazione(2.5,0), Frazione(1,2), Frazione(2,4), Frazione(3,5)
     , Frazione(6,9), Frazione(4,7), Frazione(24,36), Frazione(12,36)
     , Frazione(40,60), Frazione(5,11), Frazione(10,45), Frazione(42,78),
        Frazione(9,15)]

l_s = semplifica(l)
fractionCompare(l, l_s)
