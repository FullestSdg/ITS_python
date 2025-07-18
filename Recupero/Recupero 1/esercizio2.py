'''
Per il numero x e per ogni numero della sequenza inserita, effettuare il controllo che il numero inserito sia effettivamente un intero e forzare l'utente ad inserire un numero intero positivo nel caso in cui questa condizione non venga rispettata.
Trovare una soluzione che eviti di scrivere codice duplicato per effettuare questa serie di controlli.
 
Suggerimento: per controllare che un numeri sia intero, usare la funzione is_integer() e isistance().

Determinato il numero x e la sequenza di interi positivi, il programma deve produrre in output:
 
stampare la sequenza
Il numero occ di occorrenze di x, ovvero  il numero di volte in cui appare x nella sequenza;
La posizione pos del primo valore uguale a x.
La somma di tutti i valori diversi da x;

Ad esempio, se l'utente inserisce come valore x il numero 3 e poi immette la sequenza: 7; 5; 1; 3; 3; 3; 11; 2; 3; 3; 0
 
il programma dovra' scrivere in output:
stampare in output la sequenza
Il numero 3 compare 5 volte nella sequenza (attenzione all'output se il numero compare 1 sola volta!)
Il numero 3 compare per la prima volta in posizione 3 nella sequenza
La somma dei valori della sequenza diversi da 3 e' 26
'''

x:int = int(input("Inserisci un numero: "))

if x < 0:

    raise ValueError("Numero inserito non valido, deve essere maggiore di 0")

def checkSequenza(lista_sequenza:list[int]) -> str:

    contatore_frequenza_x = 0

    for numbers in lista_sequenza:
        
        if numbers == x:

            contatore_frequenza_x += 1 

        else:
            continue
    
    pos_x = 0

    for numbers in lista_sequenza:

        if contatore_frequenza_x == 1:

            if numbers == x:

                pos_x += lista_sequenza.index(x)

        else:

            if numbers == x:

                new_pos_x = lista_sequenza.index(x)

                pos_x = new_pos_x

    somma_valori_diversi_x = 0

    for numbers in lista_sequenza:

        if numbers != x:

            somma_valori_diversi_x += numbers 
        
        else:
            continue
    
    return f"La sequenza è {lista_sequenza}.\nIl numero {x} compare {contatore_frequenza_x} volte nella sequenza.\nIl numero {x} compare per la prima volta in posizione {pos_x} della sequenza.\nLa somma dei valori della sequenza diversi da {x} è {somma_valori_diversi_x}"

lista_sequenza = []

while True:

    numero_della_sequenza:int = int(input("Inserisci una sequenza di numeri, digitare 0 per fermare: "))

    if numero_della_sequenza == 0:
        print(checkSequenza(lista_sequenza))
        break

    elif numero_della_sequenza < 0:
        raise ValueError("Errore il numero inserito non è positivo")
    
    else:
        lista_sequenza.append(numero_della_sequenza)


