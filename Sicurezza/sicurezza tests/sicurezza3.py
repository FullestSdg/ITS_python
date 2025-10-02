# ===============================
# 1. Definizione delle chiavi RSA
# ===============================

# Modulo n = p * q
# Qui ho scelto due primi relativamente piccoli
p = 3557
q = 2579
n = p * q  # Modulo
phi = (p - 1) * (q - 1)

# Esponente pubblico
e = 3

# Calcolo dell'inverso modulare per ottenere d (esponente privato)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Non esiste inverso modulare')
    else:
        return x % m

d = modinv(e, phi)

print("Chiave pubblica (n, e):", (n, e))
print("Chiave privata (n, d):", (n, d))

# ===============================
# 2. Messaggio da cifrare
# ===============================
M = "Viva il calcio"
print("\nMessaggio originale:", M)

# Conversione in intero
Mi = int(M.encode("utf-8").hex(), 16)

# ===============================
# 3. Cifratura: C = Mi^e mod n
# ===============================
C = pow(Mi, e, n)
print("Messaggio cifrato (intero):", C)

# ===============================
# 4. Decifratura: D = C^d mod n
# ===============================
D = pow(C, d, n)

# Conversione in esadecimale
D_hex = format(D, "x")
if len(D_hex) % 2 != 0:
    D_hex = "0" + D_hex

# Conversione in stringa UTF-8
testo = bytes.fromhex(D_hex).decode("utf-8")
print("Messaggio decifrato:", testo)