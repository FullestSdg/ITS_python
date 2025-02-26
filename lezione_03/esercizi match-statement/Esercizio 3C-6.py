animale:str = input("Inserire un animale: ")
habitat:str = input("Inserire l'habitat in cui vive questo animale: ")

mammiferi:list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list = ["squalo", "trota", "salmone", "carpa"]

animal_type:list = []

dizionario_animale:dict = {"animale" : animale, "habitat": habitat, "categoria" : animal_type}

match animale:

    case animale if animale in mammiferi:
        print(f"{animale} fa parte della categoria mammiferi")
        animal_type.append(animale)

        if animale in animal_type:
            animal_type = "mammiferi"
            

            match habitat:

                case "terra":

                    if animale ==  "balena" or animale == "delfino":
                       print(f"Non ho mai visto {animale} vivere sulla terra")
                    else:
                       print(f"L'animale {animale} è uno dei {animal_type} che può vivere sulla terra")
                
                case "acqua":

                    if animale == "balena" or animale == "delfino":
                        print(f"L'animale {animale} è uno dei {animal_type} che può vivere nell'acqua")
                    else:
                        print(f"Non ho mai visto {animale} vivere nell'acqua")
                
                case "aria":
                    print(f"{animale} non può vivere in aria")

                case _:
                    print()
                



    case animale if animale in rettili:
        print(f"{animale} fa parte della categoria rettili")

    case animale if animale in uccelli:
        print(f"{animale} fa parte della categoria uccelli")

    case animale if animale in pesci:
        print(f"{animale} fa parte della categoria pesci")

    case _:
        print(f"Non so definire a quale categoria appartenga {animale}\nNon so definire a quale habitat appartenga {animale}")
