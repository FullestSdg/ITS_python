# Scrivi una funzione prodotto_top(vendite) che, dato un dizionario con prodotti e quantità vendute, ritorna il nome del prodotto più venduto.

def prodotto_top(vendite:dict[str: int]) -> str:

    max_vendite = 0
    prodotto_più_venduto = ""

    for prodotto, venduto in vendite.items():

        if venduto > max_vendite:

            max_vendite = venduto 

            prodotto_più_venduto = prodotto

    return prodotto_più_venduto

vendite = prodotto_top({"pane": 2, "uova": 3, "carne": 10, "pesche": 5})
print(vendite)