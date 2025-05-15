'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario
con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.
'''
'''
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    prodotti_scontati:dict[str:float] = {}
    
    for p,v  in prodotti.items():

        if v > 20:
            prezzo_scontato = (v * 10) / 100
            prodotti_scontati.update(prezzo_scontato)
    
    return prodotti_scontati
'''

#risultato = filtra_e_mappa({"Zaino" : 25.0, "Penna" : 10.0, "Sciarpa" : 55.0})
#print(risultato)

def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:
    prodotti_scontati: dict[str, float] = {}

    for p,v in prodotti.items():
        if v > 20:
            prezzo_scontato = v - (v * 10) / 100 
            prodotti_scontati[p] = prezzo_scontato 
    
    return prodotti_scontati

risultato = filtra_e_mappa({"Zaino": 25.0, "Penna": 10.0, "Sciarpa": 55.0})
print(risultato)
            

        