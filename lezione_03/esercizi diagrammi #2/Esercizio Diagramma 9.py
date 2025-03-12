while True:

    n:float = float(input("Inserire un numero intero positivo: "))

    if n > 0 and n % 1 == 0:
        
        contatore = 0
        i = 0

        while i <= 10:

            x:int = int(input("Inserire un numero intero: "))
            i += 1

            if x % n == 0:
                contatore += 1
            
            else:
                continue

        print(f"I numeri divisibili per {n} sono: {contatore}")
        break
        

    else:
        print("Numero inserito non valido, deve essere intero positivo")
        break