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