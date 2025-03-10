pari = 0
dispari = 0

for cont in range(10):
    n = int(input("Inserire un numero: "))

    if n % 2 == 0:
        pari += 1

    elif n % 2 == 1:
        dispari += 1

print(f"Numeri pari: {pari}\nNumeri dispari: {dispari}")