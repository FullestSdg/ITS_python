'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica
i numeri in liste separate per numeri pari e dispari.
'''

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    lista_pari:list[int] = []
    lista_dispari:list[int] = []

    for n in lista:
        if n % 2 == 0:
            lista_pari.append(n)
        else:
            lista_dispari.append(n)

    return {"pari" : lista_pari, "dispari" : lista_dispari}

risultato = classifica_numeri([1,2,3,4,5,6])
print(risultato)