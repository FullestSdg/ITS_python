# Data una lista di tuple (prodotto, categoria), crea una funzione raggruppa(lista) che restituisce un dizionario dove le chiavi sono le categorie e i valori sono liste di prodotti.

prodotti:list[tuple] = [("lavatrice", "elettrodomestico"), ("mela", "frutta"), ("aspira polvere", "elettrodomestico"), ("latte", "latticini"), 
                        ("frigorifero", "elettrodomestico")]


def raggruppa(prodotti:list[tuple[str, str]]) -> dict[str: list[str]]:

    categoria_prodotti:dict[str : list[str]] = {}

    for product, categoria in prodotti:

        if categoria not in categoria_prodotti:

            categoria_prodotti[categoria] = []

        categoria_prodotti[categoria].append(product)

    return categoria_prodotti

risultato = raggruppa(prodotti=prodotti)
print(risultato)

        





