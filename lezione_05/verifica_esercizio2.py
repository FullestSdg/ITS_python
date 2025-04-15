'''
Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista.
 Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

Il tuo compito è individuare i numeri mancanti.

Scrivi una funzione che, data in input una lista, 
restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale
'''

def find_disappeared_numbers(nums: list[int]) -> list[int]:

    n = len(nums)

    tutti_nums:list[int] = [n for n in range(1, n+1)]

    for i in tutti_nums:

        if i in tutti_nums:

            tutti_nums.remove(i)

        else:
            continue

    return tutti_nums
     
risultato = find_disappeared_numbers([1,5,1,4,3])
print(risultato)