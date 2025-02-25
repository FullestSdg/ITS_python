voto_laurea:int = int(input("Inserire un numero compreso tra 66 e 110: "))

match voto_laurea:
    
    case voto_laurea if voto_laurea <= 110 and voto_laurea >= 106:
         print(f"Voto Laurea: {voto_laurea}\nGPA: 4.0")

    case voto_laurea if voto_laurea <= 105 and voto_laurea >= 101:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 3.7")

    case voto_laurea if voto_laurea <= 100 and voto_laurea >= 96:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 3.3")

    case voto_laurea if voto_laurea <= 95 and voto_laurea >= 91:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 3.0")

    case voto_laurea if voto_laurea <= 90 and voto_laurea >= 86:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 2.7")
    
    case voto_laurea if voto_laurea <= 85 and voto_laurea >= 81:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 2.3")

    case voto_laurea if voto_laurea <= 80 and voto_laurea >= 76:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 2.0")
    
    case voto_laurea if voto_laurea <= 75 and voto_laurea >= 70:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 1.7")

    case voto_laurea if voto_laurea <= 69 and voto_laurea >= 66:
        print(f"Voto Laurea: {voto_laurea}\nGPA: 1.0")
    
    case _:
        print("Voto inserito non valido")