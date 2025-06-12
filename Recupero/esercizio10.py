'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}
'''
import string

def count_unique_words(text:str) -> dict[str,int]:

    text_lower = text.lower()
    text_splitted = text_lower.split()
    dizionario_parole_uniche:dict[str,int] = {}
    contatore = 0

    for parola in text_splitted:

        if parola[-1] not in list(string.punctuation):

            if parola not in dizionario_parole_uniche:

                dizionario_parole_uniche[parola] = contatore + 1

            else:
                dizionario_parole_uniche[parola] += contatore + 1
        
        else:

            new_parola = parola

            if new_parola not in dizionario_parole_uniche:

                dizionario_parole_uniche[parola] = contatore + 1

            else:
                dizionario_parole_uniche[parola] += contatore + 1
    
    return dizionario_parole_uniche

print(count_unique_words("ciao! mi chiamo ciao, ciao mi ciao   mi ciao, giuseppe, CIAO"))






def bin_search(lista:list, num:int) -> None:

    mid:int = len(lista) // 2

    if lista(mid) ==  num:

        print(f"Numero trovato in posizione {mid}")

    elif len(lista) == 1:

        print("Numero non trovato")

    elif lista[mid] > num:

        bin_search(lista[:mid], num)

    elif lista[mid] <  num:

        bin_search(lista[mid+1], num)


def bin_search_iterative(lista:list, num:int):

    i, j = 0, len(lista) - 1

    while True:

        mid = len(lista[i: j]) // 2

        if lista[mid] == num:

            print("Ho trovato il numero!")
        
        elif num < lista[mid]:

            j = mid -1

        elif num > lista[mid]:

            i = mid +1


    
