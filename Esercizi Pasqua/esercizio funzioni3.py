'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
'''
   
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    lista_senza_valori_rimossi:list[int] = []
    da_rimuovere_copia = da_rimuovere.copy()

    for n in lista:
        
        if n in da_rimuovere_copia and da_rimuovere_copia[n] > 0:
            da_rimuovere_copia[n] -= 1
        else:
            lista_senza_valori_rimossi.append(n)

    return lista_senza_valori_rimossi
    

risultato = rimuovi_elementi([1,2,3,2,4,5], {2 : 1})
print(risultato)

lista2:list[int] = [1,2,3,2,4,5,5]
da_rimuovere2:dict[int:int] = {2:1, 5:1}
lista_senza_valori_rimossi2:list[int] = []
da_rimuovere_copia2 = da_rimuovere2.copy()


for n in lista2:
        
    if n in da_rimuovere_copia2 and da_rimuovere_copia2[n] > 0:
        print(da_rimuovere_copia2[n])
        da_rimuovere_copia2[n] -= 1
    else:
        lista_senza_valori_rimossi2.append(n)

print(lista_senza_valori_rimossi2)
