'''
3. Catalogo prodotti
Hai un dizionario:
'''

magazzino = {"mela": 10, "banana": 5, "arancia": 8}

# Aggiungi 5 mele in magazzino. Se il prodotto non esistesse, aggiungilo con quella quantità.

magazzino["mela"] = 10 +5

magazzino["avocado"] = 0

item_rimossi:dict[str : int] = {}

item_rimosso = (magazzino.pop("avocado"))

item_rimossi["avocado"] = item_rimosso

print(magazzino)
print(item_rimossi)

