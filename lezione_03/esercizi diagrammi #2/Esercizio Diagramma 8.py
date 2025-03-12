A:float = float(input("Inserire un numero: "))
B:float = float(input("Inserire un numero: "))

while True:

    if A < B:

        if A > 0 and B > 0:


            if A % 1 == 0 and B % 1 == 0:

                sum = 0
                i = A

                while i <= B:

                        sum += i
                        i += 1

                print(sum)
                break

            else:
                print(f"Errore {A} e {B} devono essere interi")
                break
        else:
            print(f"Errore {A} e {B} devono essere positivi")
            break
    else:
        print(f"Errore {A} deve essere minore di {B}")
        break
