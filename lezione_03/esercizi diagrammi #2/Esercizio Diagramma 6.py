x:int = int(input("Inserisci un numero: "))
sum = 0

if x > 0:

    i = 0
    while True:

        n:int = int(input("Inserisci 10 numeri, sia positivi che negativi: "))

        i += 1

        if i == 11:

            print(sum)
            break

        if x % 2 == 0:

            if n > x/2:
                sum += n
            else:
                continue
        else:
            if n <= x:
                sum += n
            else:
                continue

elif x < 0:
    print(f"Errore {x} deve essere positivo")