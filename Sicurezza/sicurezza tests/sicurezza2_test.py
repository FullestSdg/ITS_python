'''
Crittografia

Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.
'''

mex = 204751668535
e = 3
n = 514948966453

# Creo una variabile booleana inizializzata a False
lo_troverò = False

# Creo un clico while che "lavora" finchè la variabile booleana è false, una volta trovato un match della parola cifrata la variabile diventa True ed il ciclo finisce

while lo_troverò == False:

    for p1 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":

        for p2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":

            for p3 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                
                for p4 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                    
                    for p5 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":

                        parola_cifrata = p1 + p2 + p3 + p4 + p5                    
                        try:
                            riuscirò_a_cifrare = int(parola_cifrata.encode("utf-8").hex(), 16) 
                            cifrato = pow(riuscirò_a_cifrare, e, n)

                            # dopo aver covertito in esadecimale eseguo l'operazione di cifratura RSA con l'esponente pubblico e il modulo n

                            if cifrato == mex:
                                print(f"TROVATA!!!!\nParola: {parola_cifrata}")
                                    
                                lo_troverò = True

                        except:
                            continue

                        # finchè non trova una corrispondenza il ciclo va avanti
