'''
🟢 Esercizio 1: Somma dei numeri pari
Scrivi una funzione somma_pari(lista) che:

Prende in input una lista di numeri interi

Restituisce la somma di tutti i numeri pari
'''

def somma_pari(numeri:list[int]) -> int:

    somma_numeri_pari = 0

    for n in numeri:

        if n % 2 == 0:

            somma_numeri_pari += n

    return somma_numeri_pari

print(somma_pari([1,2,3,4,5,6,7,8,9,10]))

