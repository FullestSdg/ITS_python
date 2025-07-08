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
    
    def __repr__(self):
        return f"{self._numeratore}/{self._denominatore}" 

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

''' 
8.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, ovvero il più grande divisore comune tra numeratore e denominatore è 1.
Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.
Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
Nello specifico:
se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.
se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.
Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.
'''

f = [Frazione(12,6),Frazione(24,8),Frazione(99,33),Frazione(6,7),Frazione(1,1)]

def semplifica(l:list[Frazione]) -> list[Frazione]:

    lista_frazioni_irriducibili:list[Frazione] = []

    for i in l:

        if mcd(i.getNumeratore(), i.getDenonminatore()) == 1:
            lista_frazioni_irriducibili.append(i)
        
        else:

            if i.getDenonminatore() / mcd(i.getNumeratore(), i.getDenonminatore()) % 2 == 0 and i.getNumeratore() / mcd(i.getNumeratore(), i.getDenonminatore()) % 2 == 0:
                denominatore_semplificato = i.getDenonminatore() / mcd(i.getNumeratore(), i.getDenonminatore())
                numeratore_semplificato = i.getNumeratore() / mcd(i.getNumeratore(), i.getDenonminatore())

                frazione = Frazione(numeratore_semplificato, denominatore_semplificato)

                lista_frazioni_irriducibili.append(frazione)

            else:
                continue
    
    return lista_frazioni_irriducibili


print(semplifica(f))






