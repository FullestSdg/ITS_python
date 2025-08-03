'''
🟢 Esercizio 3 – Somma dei quadrati dispari
Scrivi una funzione somma_quadrati_dispari(numeri) che:

Prende in input una lista di numeri interi

Eleva al quadrato solo i numeri dispari

Ritorna la somma di questi quadrati
'''

def somma_quadrati_dispari(numeri:list[int]) -> int:

    somma_numeri = 0

    for n in numeri:

        if n % 2 != 0:

            somma_numeri += n**2

    return somma_numeri

print(somma_quadrati_dispari([1,2,3,4,5]))

