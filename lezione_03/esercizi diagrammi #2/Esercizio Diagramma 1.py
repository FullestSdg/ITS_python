max_posti:int = int(input("Inserire un numero di posti: "))

liberi:int = max_posti

while True:
    opzione:str = input("Inserire un'opzione: ").lower()

    match opzione:

        case "ingresso":

            if liberi > 0:
                liberi -= 1
            else:
                print("Non ci sono posti disponibili")

        case "uscita":

            if liberi < max_posti:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")

        case "stato":

            print(liberi)
            print(max_posti - liberi)

        case "esci":

            break

        case _: 

            print(f"{opzione} non è un'opzione valida!")

