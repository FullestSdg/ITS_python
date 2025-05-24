'''
🟢 Esercizio 2: Filtro parole
Scrivi una funzione filtra_parole(lista_parole, lunghezza) che:

Riceve una lista di parole e un numero intero

Restituisce una nuova lista contenente solo le parole con lunghezza maggiore o uguale a lunghezza

'''

def filtra_parole(lista_parole:list[str], lunghezza:int) -> list[str]:

    parole_lunghezza_maggiore:list[str] = []

    for parola in lista_parole:

        if len(parola) >= lunghezza:

            parole_lunghezza_maggiore.append(parola)

    return parole_lunghezza_maggiore

print(filtra_parole(["ciao", "francesco", "DAJE ROMA DAJE YAHOOOOOOOOOOOOOOOO", "AOOOOOOOOOOOOOOOOOOOO"], 10))

    