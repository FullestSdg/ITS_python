nome:str = input("Inserire il tuo nome: ")
gender:str = input("Inserire il tuo genere (inserire m o f): ")

match gender:

    case "m":
        print(f"Nome: {nome}\n Genere: Maschio")

    case "f":
        print(f"Nome: {nome}\nGenere: Femmina")

    case _:
        print("Genere inserito non valido, impossibile stampare un documento di identità")