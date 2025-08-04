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

# Versione mia più simpatica
x = 71
y = 44

def calcolosomma(x:int, y:int) -> int:

    prodotti:list[int] = []
    
    for i in range(2,y+1,2):
        i *= x 
        prodotti.append(i)

    return prodotti[-1]

def proDict() -> dict[tuple[int],list[int]]:
    return {(x,y) : calcolosomma(x,y)}


print(proDict())

# Versione chatgpt
def proDict() -> dict[tuple[int, int], int]:
    dizionario = {}
    for x in range(0, 101):        # x da 0 a 100
        for y in range(2, 89, 2):  # y pari da 2 a 88
            dizionario[(x, y)] = x * y
    return dizionario

# Main
d = proDict()

# Esempio: stampiamo 3 risultati richiesti
# print(d[(13, 88)])  # Output: 1144
# print(d[(83, 56)])  # Output: 4648
print(d[(71, 44)])  # Output: 3124