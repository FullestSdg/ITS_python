oggetti:list = []

i = 0
while i < 3:
    oggetti.append(input("Inserire un oggetto: "))
    i += 1

match oggetti:

    case ["penna","matita", "quaderno"]:
        print("Materiale Scolastico")   

    case ["pane", "latte", "uova"]:
        print("Prodotti Alimentari")
    
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")

    case ["telefono", "computer", "tablet"]:
        print("Dispositivi Elettronici")

    case _:
        print("Categoria sconosciuta")
