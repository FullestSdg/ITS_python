somma:float = 0
contatore:float = 0

while True:
    n:float = float(input("Inserire un numero: "))
    contatore += 1

    if n > 0:
        somma += n

    if contatore == 5:
        break

print(f"La somma dei numeri positivi è: {somma}")