while True:
    n:int = int(input("Inserisci un numero intero positivo: "))

    if n > 0:

        i = 1
        fattoriale = 1
        for numbers in range(n):

             if i != n:
              fattoriale *= i
              i += 1

        print(fattoriale)

    else:
        print("Numero inseri non valido")
        break
