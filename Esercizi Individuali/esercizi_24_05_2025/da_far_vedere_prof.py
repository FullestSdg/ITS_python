'''
Esercizio 4: Simulazione "Indovina il numero"
Scrivi una funzione indovina_numero(numero_segreto, tentativi) che:

Prende in input un numero segreto tra 1 e 10 e una lista di tentativi dell’utente

Per ogni tentativo:

Stampa "Troppo alto", "Troppo basso" o "Corretto!"

Se il numero è corretto, termina la funzione

Se nessun tentativo è corretto, stampa "Hai perso!"

(usa for, if, break, continue)
'''

def indovina_numero(numero_segreto:int, tentativi:list[int]) -> str:

    while len(tentativi) > 0:
    
        for tentativo in tentativi:

            if tentativo > numero_segreto:

                return "Troppo alto"
            
            elif tentativo == numero_segreto:

                return "Corretto!"
             
            else:

                return "Troppo basso"
            
        tentativi.pop()

        if tentativi == 0:

            break

print(indovina_numero(5, [1,2,3,9,8,5]))

# da far vedere prof


