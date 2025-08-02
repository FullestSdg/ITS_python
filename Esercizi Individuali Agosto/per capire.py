'''
Esercizio 2.

Si vuole calcolare la somma di tutti i prodotti x * y per tutti i valori interi di x (i cui valori variano tra 0 e 100) e tutti i valori interi di y (i cui valori sono dati dalla sequenza 2, 4, 6, 8, 10, 12, ..., 88), ovvero i prodotti
1 * 2,
1 * 4,
...
1 * 88,
2 * 2,
2 * 4,
...
2 * 88,
...
100 * 2,
100 * 4,
...
100 * 88

Scrivere una funzione Python proDict() che senza ricevere alcun argomento in input, che restituisce un dizionario che abbia come chiavi la tupla (x,y) e come valore x*y , in cui memorizzare tutti i prodotti x * y per tutti i valori interi di x e tutti i valori interi di y.

Nel main, scrivere un codice Python che inizializzi un dizionario d ricorrendo alla funzione prodDict e stampare in output i valori del dizionario d, per i seguenti valori di x e y:
x = 13, y = 88
x = 83, y = 56
x = 71, y = 44
'''
# x = 13
# y = 88
# x = 83
# y = 56
x = 2
y = 6

def calcolosomma(x:int, y:int) -> int:

    prodotti:list[int] = []
    
    for i in range(2,y+1,2):
        i *= x 
        prodotti.append(i)

    return prodotti[-1]

def proDict() -> dict[tuple[int],list[int]]:

    return {(x,y) : calcolosomma(x,y)}


print(proDict())