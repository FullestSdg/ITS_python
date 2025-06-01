# Scrivi una funzione totale_carrello(carrello) dove carrello è un dizionario con nomi di prodotti e prezzi. Calcola il totale.

def totale_carrello(carrello:dict[str : float]) -> float:

    costo_totale = 0

    for oggetti, prezzo in carrello.items():

        costo_totale += prezzo

    return float(costo_totale)

costo_spesa = totale_carrello({"pane": 4.5, "succo_di_frutta": 2, "pasta": 1.99, "carne": 5.67})
print(costo_spesa)

