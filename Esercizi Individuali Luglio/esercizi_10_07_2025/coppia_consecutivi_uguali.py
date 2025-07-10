'''
Esercizio 3 – Indici di due elementi consecutivi uguali (6 punti)
Scrivere una funzione coppia_consecutivi_uguali(L) che riceva una lista L e restituisca la prima coppia di indici consecutivi [i, i+1] tali che L[i] == L[i+1].

Potete assumere:

esiste almeno una coppia di elementi consecutivi uguali.

Esempio:

python
Copia
Modifica
L = [1, 2, 3, 3, 5, 6, 6]
print(coppia_consecutivi_uguali(L))  # output atteso: [2, 3]

'''

def coppia_consecutivi_uguali(L:list[int]) -> list[int]:

    for i in range(len(L)):

        for j in range(i + 1,len(L)):

            if L[i] == L[j]:

                return [i,j]
            
            else:
                continue

print(coppia_consecutivi_uguali([1, 2, 3, 3, 5, 6, 6]))