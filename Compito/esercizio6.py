#Esercizio n.6

n1:int = int(input("Inserire un numero intero: "))
n2:int = int(input("Inserire un numero intero: "))

prodotto = 1
if n1 < n2:
    for i in range(n1, n2 + 1):
     prodotto *= i
    print(f"Il prodotto dei numeri tra {n1} e {n2} è: {prodotto}")

elif n1 > n2:
    for i in range(n2, n1 + 1):
     prodotto *= i
    print(f"Il prodotto dei numeri tra {n1} e {n2} è: {prodotto}")