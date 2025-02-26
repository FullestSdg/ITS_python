#Esercizio n.4
numeri:list = []
numeri_interi:list = []
somma_interi:int = 0
contatore_interi:int = 0

while True:
    n:float = float(input("Inserire un numero: "))
    
    if n < 0:
        break

    numeri.append(n)

    if n.is_integer():
        numeri_interi.append(n)
        somma_interi += n
        contatore_interi += 1

if contatore_interi > 0:
    media_numeri = somma_interi / contatore_interi
    print(f"La media dei numeri interi è: {media_numeri}")
else:
    print("Non sono stati inseriti numeri interi.")

if len(numeri) > 0:
    max_numeri = numeri[0]
    min_numeri = numeri[0]
    for i in numeri:
        if i > max_numeri:
            max_numeri = i
        if i < min_numeri:
            min_numeri = i

    print(f"Il numero più grande è: {max_numeri}.")
    print(f"Il numero più piccolo è: {min_numeri}.")
else:
    print("Non sono stati inseriti numeri.")