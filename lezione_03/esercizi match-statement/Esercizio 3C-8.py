frase:str = input("Inserire una frase: ")

ultimo_carattere:str = frase[-1]

match frase:

    case frase if ultimo_carattere == "?" and len(frase) % 2 == 0:
        print("Si")

    case frase if ultimo_carattere == "?" and len(frase) % 2 == 1:
        print("No")

    case frase if ultimo_carattere == "!":
        print("Wow")
    
    case _:
        print(f"Tu dici {frase}")