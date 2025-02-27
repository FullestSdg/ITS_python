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
                    print("Habitat inserito non valido")
                

    case animale if animale in rettili:
        print(f"{animale} fa parte della categoria rettili")
        animal_type.append(animale)

        if animale in animal_type:
            animal_type = "rettili"
            

            match habitat:

                case "acqua":

                    if animale ==  "lucertola" or animale == "serpente":
                       print(f"Non ho mai visto {animale} vivere nell'acqua")
                    else:
                       print(f"L'animale {animale} è uno dei {animal_type} che può vivere nell'acqua")
                
                case "terra":

                    if animale == "tartaruga" or animale == "coccodrillo":
                        print(f"L'animale {animale} è uno dei {animal_type} che può anche vivere sulla terra")
                    else:
                        print(f"L'animale {animale} è uno dei {animal_type} che può vivere sulla terra")
                
                case "aria":
                    print(f"{animale} non può vivere in aria")

                case _:
                    print("Habitat inserito non valido")

    case animale if animale in uccelli:
        print(f"{animale} fa parte della categoria uccelli")
        animal_type.append(animale)

        if animale in animal_type:
            animal_type = "uccelli"
            

            match habitat:

                case "terra":

                    if animale ==  "gallina" or animale == "tacchino":
                       print(f"L'animale {animale} è uno degli {animal_type} che può vivere sulla terra")

                    else:
                       print(f"Non ho mai visto {animale} vivere sulla terra")
                
                case "acqua":

                    if animale == "anatra" or animale == "cigno":
                        print(f"L'animale {animale} è uno degli {animal_type} che può vivere nell'acqua")
                    else:
                        print(f"Non ho mai visto {animale} vivere nell'acqua")
                
                case "aria":

                    if animale == "gufo" or animale == "falco" or animale == "aquila" or animale == "pappagallo":
                        print(f"L'animale {animale} è uno dei {animal_type} che può vivere in aria")

                    else:
                        print(f"Non ho mai visto {animale} vivere in aria")

                case _:
                    print("Habitat inserito non valido")

    case animale if animale in pesci:
        print(f"{animale} fa parte della categoria pesci")
        animal_type.append(animale)

        if animale in animal_type:
            animal_type = "pesci"
            

            match habitat:

                case "terra":
                       print(f"Non ho mai visto {animale} vivere sulla terra")
                
                case "acqua":
                    print(f"Lanimale {animale} è uno dei {animal_type} che può vivere in acqua")

                case "aria":
                    print(f"{animale} non può vivere in aria")

                case _:
                    print("Habitat inserito non valido")

    case _:
        print(f"Non so definire a quale categoria appartenga {animale}\nNon so definire a quale habitat appartenga {animale}")