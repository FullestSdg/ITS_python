n:int = int(input("Inserire un numero: "))

i = 0

while i != n:

    x:int = int(input("Inserisci un numero: "))
    y:int = int(input("Inserisci un numero: "))

    if x > 0 and y > 0:
        result = x*y
        print(result)

    elif x < 0 and y < 0:
        print("Errore")

    else:
        result = x-y
        print(result)

    i += 1

    