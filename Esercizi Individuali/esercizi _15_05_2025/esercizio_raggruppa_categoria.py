# Data una lista di tuple (prodotto, categoria), crea una funzione raggruppa(lista) che restituisce un dizionario dove le chiavi sono le categorie e i valori sono liste di prodotti.

prodotti:list[tuple] = [("lavatrice", "elettrodomestico"), ("mela", "frutta"), ("aspira polvere", "elettrodomestico"), ("latte", "latticini"), 
                        ("frigorifero", "elettrodomestico")]


def raggruppa(prodotti:list[tuple]) -> dict[str: list]:

    lista_prodotti:list[str] = []
    lista_categoria:list[str] = []

    for product in prodotti:

        lista_prodotti.append(product[0])

        if product[1] in lista_categoria:

            lista_categoria.append(product[1])

    return {str(lista_categoria) : lista_prodotti}

risultato = raggruppa(prodotti=prodotti)
print(risultato)

        





