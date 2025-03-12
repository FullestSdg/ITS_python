while True:
    n:float = float(input("Inserire un numero intero: "))

    if n % 1 == 0:

        if n % 2 == 0 and n > 10:
            print("Numero Valido")
        
        else:
            print("Numero non valido")
    
    else:
        print("Devi inserire un numero intero!")
        continue
