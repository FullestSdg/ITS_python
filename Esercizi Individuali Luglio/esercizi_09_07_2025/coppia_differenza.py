'''
Esercizio 1 – Coppia con somma più vicina a un target (6 punti)
Scrivere una funzione coppia_somma_target(L, T) che riceva:

una lista L contenente solo numeri (almeno due),

un valore T (target numerico),

e restituisca la coppia di indici [i, j] con i < j tale che la somma L[i] + L[j] sia la più vicina possibile a T, in valore assoluto.

Potete assumere che:

L contiene almeno due numeri,

la coppia che produce la somma più vicina a T è unica.

Esempio:

python
Copia
Modifica
L = [1, 4, 8, 12, 5]
T = 10
print(coppia_somma_target(L, T))  # output atteso: [1, 4]

'''

def coppia_somma_target(L:list[int],T:int) -> list[int]:

    pos_indici = [0, 1]
    min_diff = abs(L[0] + L[1] - T)

    for i in range(len(L)):

        for j in range(i + 1, len(L)):

            somma_corrente = L[i] + L[j]
            diff = abs(somma_corrente - T)

            if diff < min_diff:
                
                min_diff = diff
                pos_indici = [i, j]

    return pos_indici

print(coppia_somma_target([1, 4, 8, 12, 5], 10))