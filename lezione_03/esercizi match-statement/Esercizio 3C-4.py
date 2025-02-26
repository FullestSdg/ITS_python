animale:str = input("Inserire il nome di un animale: ")

mammiferi:list = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list = ["aquila", "pappagallo", "gufo", "falco"]
pesci:list = ["squalo","trota", "salmone", "carpa"]

match animale:

    case animale if animale in mammiferi:
        print(f"{animale} fa parte della categoria mammiferi")

    case animale if animale in rettili:
        print(f"{animale} fa parte della categoria rettili")

    case animale if animale in uccelli:
        print(f"{animale} fa parte della categoria uccelli")

    case animale if animale in pesci:
        print(f"{animale} fa parte della categoria pesci")

    case _:
        print(f"Non so definire a quale categoria appartenga {animale}")