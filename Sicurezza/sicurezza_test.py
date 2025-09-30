
# openssl genrsa -out FAprivkey.pem -3 2048

# openssl rsa -in FAprivkey.pem -out FApubkey.pem -pubout -RSAPublicKey_out

'''
• Per cifrare e poi decifrare, il comando si basa su
• openssl pkeyutl -h
• openssl pkeyutl -encrypt -inkey FApubkey.pem -pubin -
in messRSA.txt -out MessaForFA.dat
•
• openssl pkeyutl -decrypt -inkey FAprivkey.pem -in
MessaForFA.dat -out MessaForFA.dec
'''
'''
n = "00b83e1f24c1955b32dd0e635ac126"+\
    "aea92b8f0c925bfbf6050ef497b731"+\
    "f42c8c656965a5b464093bcd3d9d83"+\
    "19c411fde9ef3a2ba2955d3e5b3708"+\
    "140f22eed316b2edd61473f7caed10"+\
    "f086a51717a3b4d89b8b7610c5320f"+\
    "9bf606b31f7acebbe5bfb0f58c0180"+\
    "6c8d9d251ab17477d9a1eb18f7ed1c"+\
    "d7f851e63c6c45f8de063e70051a4c"+\
    "8535d1412a3fb447b34e3fe71f991f"+\
    "14bb810ce82eb3b92462ebb581a204"+\
    "cc2bec63a35051f52e3c9b4a6f8f00"+\
    "fd59ad9f6039f7bd86f80833cd81df"+\
    "a0975b4de029845aa4a2841339c7d5"+\
    "d72abbba96388ba00a932b45271767"+\
    "ce7eb8533f59157ce3402fd2f06a94"+\
    "8fb333d6a405a5e1d8fdb31708e03c"+\
    "e82f"


decimale = int(n, 16)

#messaggio;
M = "VIVA EL FOOTBALL YILDIZ"
Mi = int(M.encode("utf-8").hex(), 16)

e = 3 

#cifrato: 
cifrato = pow(Mi, e, decimale)
print(cifrato)

d = "MIIBCAKCAQEAuD4fJMGVWzLdDmNawSauqSuPDJJb+/YFDvSXtzH0LIxlaWWltGQJ"+\
    "O809nYMZxBH96e86K6KVXT5bNwgUDyLu0xay7dYUc/fK7RDwhqUXF6O02JuLdhDF"+\
    "Mg+b9gazH3rOu+W/sPWMAYBsjZ0lGrF0d9mh6xj37RzX+FHmPGxF+N4GPnAFGkyF"+\
    "NdFBKj+0R7NOP+cfmR8Uu4EM6C6zuSRi67WBogTMK+xjo1BR9S48m0pvjwD9Wa2f"+\
    "YDn3vYb4CDPNgd+gl1tN4CmEWqSihBM5x9XXKru6ljiLoAqTK0UnF2fOfrhTP1kV"+\
    "fONAL9LwapSPszPWpAWl4dj9sxcI4DzoLwIBAw=="

decimale1 = int(d, 16)

M = cifrato 
Mi2 = int(M.encode("utf-8").hex(), 16)

cifrato2 = pow(Mi2, e, decimale1)
print(cifrato2)
'''

# openssl dgst -hex -sha256 mess1.txt

'''


Crittografia

Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.

'''

# e = 3
# n = 514948966453

# Messaggio = 204751668535


import math
from typing import Tuple, Optional

n = 514948966453
e = 3
c = 204751668535

def trial_factor(n: int) -> Optional[Tuple[int,int]]:
    """Prova a fattorizzare n con divisione fino a sqrt(n). Restituisce (p,q) o None."""
    lim = int(math.isqrt(n)) + 1
    # saltiamo i pari dopo 2 per velocizzare un po'
    if n % 2 == 0:
        return 2, n//2
    p = 3
    while p <= lim:
        if n % p == 0:
            return p, n // p
        p += 2
    return None

def egcd(a: int, b: int):
    if b == 0:
        return (1, 0, a)
    x, y, g = egcd(b, a % b)
    return (y, x - (a // b) * y, g)

def invmod(a: int, m: int) -> Optional[int]:
    x, y, g = egcd(a, m)
    if g != 1:
        return None
    return x % m

def int_to_ascii(m: int) -> str:
    """Converte un intero in bytes big-endian e poi in stringa ASCII."""
    length = (m.bit_length() + 7) // 8
    b = m.to_bytes(length, byteorder='big')
    try:
        return b.decode('ascii')
    except UnicodeDecodeError:
        # se non è ascii pura, mostra i bytes grezzi
        return repr(b)

def main():
    fac = trial_factor(n)
    if fac is None:
        print("Non sono riuscito a fattorizzare n con trial division (troppo grande).")
        return
    p, q = fac
    if p > q:
        p, q = q, p
    print(f"Trovati fattori: p = {p}, q = {q}")

    # calcolo l = lcm(p-1, q-1)
    g = math.gcd(p-1, q-1)
    l = (p-1)*(q-1) // g
    print(f"l = lcm(p-1,q-1) = {l}")

    d = invmod(e, l)
    if d is None:
        print("e non invertibile modulo l; impossibile calcolare d.")
        return
    print(f"Esponente privato d = {d}")

    m = pow(c, d, n)
    print(f"M numerico (m) = {m}")
    plaintext = int_to_ascii(m)
    print(f"Messaggio decifrato: {plaintext}")

if __name__ == "__main__":
    main()
