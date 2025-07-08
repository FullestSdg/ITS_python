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

l = [Frazione(10,45),Frazione(24,8),Frazione(99,33),Frazione(6,7),Frazione(1,1)]
print(l)
f = (semplifica(l))
print(f)


'''
8.D Scrivere in Python una funzione chiamata fractionCompare() che prende in input la lista di frazioni l originale e la lista con le frazioni di l semplificata.
 
Usando il metodo value(), dimostrare che il valore di ogni funzione di entrambe le liste non cambia, stampandolo in output.
Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538
   

8.E Scrivere un codice Python che inizializzi la seguente lista l di frazioni, dove ogni frazione è un oggetto della classe Frazione:
 
l = 2.5/0,   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15
       
Sfruttando la funzione semplifica, generare una nuova lista chiamata l_s, contente una versione semplificata delle frazioni della lista l.
Infine, richiamando la funzione fractionCompare, dimostrare che le funzioni delle lista l e l_s sono equivalenti, ovvero hanno lo stesso valore.
'''

def fractionCompare(l:list[Frazione], f:list[Frazione]) -> float:


    while len(l) > 0:      
        
        print(f"Valore frazione originale: {l[0].value()} --- Valore frazione ridotta: {f[0].value()}")
        l.pop(0)

print(fractionCompare(l, f))

