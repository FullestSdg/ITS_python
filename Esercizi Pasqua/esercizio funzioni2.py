'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. 
Se ci sono valori duplicati, scarta i duplicati.
'''

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    dizionario_invertito:dict[int:str] = {}

    for chiave,valore in dizionario.items():

        if valore not in dizionario_invertito:
            dizionario_invertito[valore] = chiave

    return dizionario_invertito

risultato = inverti_mappa({"ciao" : 12, "ciao2" : 24})
print(risultato)