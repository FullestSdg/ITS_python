'''
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
'''

def integerPower(base:int, esponente:int) -> int:

    while True:
        
        if base % 1 == 0 and esponente != 0 and esponente % 1 == 0:
            risultato = base ** esponente
            break

        else:
            raise ValueError("Errore base o esponente non validi")
    
    return risultato

risultato = integerPower(-2,0)
print(risultato)


    
