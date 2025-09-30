'''

Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...
'''

from Crypto.Cipher import *
from Crypto.Util.number import inverse 

C = 10002041662569686
n = 51151902024533551
e = 3

for numbers in range(1+1, n): # tutti i numeri che vanno da 2 a n    
    p = 1 # altrimenti divide per 0

    if n % numbers == 0: 

        p = numbers
        break

q = n // p  # formula inversa dato che abbiamo sia n che p

phi = (p-1)*(q-1)
d = inverse(e, phi) 
cifrato = pow(C, d, n)


l = ((cifrato.bit_length() + 7) // 8) # lunghezza messaggio in byte

mg = cifrato.to_bytes(l, "big") # il messaggio va in base al byte più significativo

mex = mg.decode("utf-8") # lo faccio diventare una stringa

print(f"Messaggio: {mex}")