'''
Esercizio 4 – Coppia più vicina sulla lista ordinata (6 punti)
Scrivere una funzione coppia_vicina_ordinata(L) che riceva una lista L di numeri, e restituisca la coppia di indici [i, j] nella lista originale corrispondenti ai due valori adiacenti più vicini tra loro dopo che la lista è stata ordinata.

Attenzione: la lista va ordinata solo per cercare la coppia, ma gli indici da restituire sono riferiti alla lista originale.

Potete assumere che esista una sola coppia con differenza minima.

Esempio:

python
Copia
Modifica
L = [10, 1, 3, 8, 2]
print(coppia_vicina_ordinata(L))  # output atteso: [2, 4]

'''

def coppia_vicina_ordinata(L: list[int]) -> list[int]:
    # Lista di tuple (valore, indice_originale)
    ordinata_con_indici = sorted((val, idx) for idx, val in enumerate(L))

    min_diff = float('inf')
    migliori_indici = [0, 1]

    for i in range(len(ordinata_con_indici) - 1):
        val1, idx1 = ordinata_con_indici[i]
        val2, idx2 = ordinata_con_indici[i + 1]
        diff = abs(val1 - val2)

        if diff < min_diff:
            min_diff = diff
            migliori_indici = sorted([idx1, idx2])

    return migliori_indici

print(coppia_vicina_ordinata([10, 201, 3, 8, 45, 5, 7, 129])) 

# da rivedere