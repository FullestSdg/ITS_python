while True:
    x:float = float(input("Inserisci un numero: "))
    y:float = float(input("Inserisci un numero: "))
    z:float = float(input("Inserisci un numero: "))

    if x % 1 == 0 and x > 0:

        if y % 1 == 0 and y > 0:

            if z % 1 == 0 and z > 0:


               if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:

                    print("Regole rispettate")
                    break

               else:
                    print("Regole non rispettate")
                    break
    
            else:
                print(f"Errore {z} deve essere intero positivo")
                continue

        else: 
            print(f"Errore {y} deve essere intero positivo")
            continue
    
    else:
        print(f"Errore {x} deve essere intero positivo")
        continue
