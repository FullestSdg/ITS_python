'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti
e aggrega i voti per studente in un nuovo dizionario.
'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    
    dizionario_voti_aggregati = {}

    for v in voti:
        for studente, voto in v.items():

            if studente not in dizionario_voti_aggregati:

                dizionario_voti_aggregati[studente] = []

            dizionario_voti_aggregati[studente].append(voto)

    return dizionario_voti_aggregati
                
risultato = aggrega_voti([{"nome" : "Alice", "voto" : 80}, {"nome" : "Alice", "voto" : 75}, {"nome" : "Bob", "voto" : 55}])
print(risultato)