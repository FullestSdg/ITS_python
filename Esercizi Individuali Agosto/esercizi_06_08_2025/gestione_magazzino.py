'''Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
Il sistema cerca un prodotto per verificare se esiste nell'inventario.
Il sistema verifica la disponibilità dei prodotti in inventario.
'''

class Prodotto:

    _nome:str 
    _quantità:int 

    def __init__(self, nome:str, quantità:int) -> None:
        self._nome = nome 
        self._quantità = quantità

    def getNome(self) -> str:
        return self._nome 
    
    def getQuantità(self) -> int:
        return self._quantità

class Magazzino:

    def __init__(self) -> None:
        self._magazzino = {}

    def aggiungi_prodotto(self, prodotto:Prodotto) -> None:
        
        if prodotto.getNome() not in self._magazzino:
            self._magazzino[prodotto.getNome()] = prodotto.getQuantità()
        
        else:
            self._magazzino[prodotto.getNome()] += prodotto.getQuantità()

    def cerca_prodotto(self, nome:str) -> Prodotto | str:
        
        if nome in self._magazzino:
            return nome, self._magazzino[nome]
        
        else:
            return "Prodotto inesistente"

    def verifica_disponibilità(self, nome:str) -> str:        
        
        if nome in self._magazzino:
            return f"Prodotto: '{nome}' disponibile!"
        
        else:
            return f"Prodotto non disponibile"


banana:Prodotto = Prodotto("banana", 20)
latte:Prodotto = Prodotto("latte", 10)
latte2:Prodotto = Prodotto("latte", 10)
magazzino_super:Magazzino = Magazzino()

magazzino_super.aggiungi_prodotto(banana)
magazzino_super.aggiungi_prodotto(latte)
magazzino_super.aggiungi_prodotto(latte2)

print(magazzino_super.cerca_prodotto("latte"))
print(magazzino_super.cerca_prodotto("uova"))
print(magazzino_super._magazzino)

print(magazzino_super.verifica_disponibilità("latte"))
print(magazzino_super.cerca_prodotto("uova"))
