'''
🟢 Esercizio 3: Generatore di dizionario
Scrivi una funzione genera_dizionario(lista) che:

Prende una lista di stringhe

Restituisce un dizionario in cui ogni stringa è chiave e il valore è la lunghezza della stringa

Usa una dictionary comprehension
'''

def genera_dizionario(lista_stringhe:list[str]) -> dict[str: int]:

    return {parola : len(parola) for parola in lista_stringhe}

print(genera_dizionario(["giuseppe", "roberto", "ciao"]))