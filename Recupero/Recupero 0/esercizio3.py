def carrello(dizionario:dict[str, int|float]) -> dict[str, int|float]:

    new_dict:dict = {}

    for prodotto, prezzo in dizionario.items():

        if prezzo <= 50:

            prezzo += (prezzo * 10) / 100

            new_dict[prodotto] = round(prezzo, 2) #float(f"{prezzo:.2f}")

    return new_dict

print(carrello({"latte": 5, "formaggio": 2.5, "lavatrice": 96, "ruspa": 150}))