'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
      
    lista_senza_valori_rimossi:list[int] = []


    for n in lista:

        if n not in da_rimuovere:

            lista_senza_valori_rimossi.append(n)
        
        elif n in da_rimuovere:

            lista_senza_valori_rimossi.remove(n)
        

    return lista_senza_valori_rimossi

risultato = rimuovi_elementi([1,2,3,2,4,5], {2 : 1})
print(risultato)