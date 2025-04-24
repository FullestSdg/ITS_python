'''
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
'''

def remove_duplicates(numeri:list[int]) -> list:

    numeri2:list[int] = []

    for n in numeri:
        if numeri.count(n) > 0 and n not in numeri2:

            numeri2.append(n)
            
    return numeri2

risultato = remove_duplicates([1,2,1,2,3,4,5,5,6])
print(risultato)

