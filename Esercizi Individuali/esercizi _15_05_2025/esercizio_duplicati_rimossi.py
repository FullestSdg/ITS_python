# Definisci una funzione rimuovi_duplicati(lista) che rimuove i duplicati da una lista mantenendo l’ordine originale.

def rimuovi_duplicati(numeri:list[int]) -> list[int]:

    numeri_non_duplicati:list[int] =[]

    for n in numeri:

        if n not in numeri_non_duplicati:
            numeri_non_duplicati.append(n)

    return numeri_non_duplicati

risultato = rimuovi_duplicati([2,2,2,3,4,5,5,7,6])
print(risultato)