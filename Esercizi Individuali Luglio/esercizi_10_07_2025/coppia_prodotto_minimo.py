'''
Esercizio 2 – Coppia con prodotto minimo (6 punti)
Scrivere una funzione coppia_prodotto_minimo(L) che riceva una lista L di almeno due numeri e restituisca la coppia di indici [i, j] (con i < j) per cui il prodotto L[i] * L[j] è il più piccolo possibile.

Potete assumere:

la lista ha almeno due numeri,

esiste una sola coppia con prodotto minimo.

Esempio:

python
Copia
Modifica
L = [-2, 3, 0, -5, 4]
print(coppia_prodotto_minimo(L))  # output atteso: [0, 3]
'''

def coppia_prodotto_minimo(L:list[int]) -> list[int]:

    if len(L) >= 2:

        prodotto_minimo_variabile = float("Inf")
        nuovo_prodotto_minimo = [0,1]

        for i in range(len(L)):

            for j in range(i + 1,len(L)):

                prodotto_minimo = L[i] * L[j]

                if prodotto_minimo < prodotto_minimo_variabile:

                    nuovo_prodotto_minimo = [i,j]
    
    return nuovo_prodotto_minimo

print(coppia_prodotto_minimo([-2, 3, 0, -5, 4]))



