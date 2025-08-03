'''
🟡 Esercizio 2 – Verifica dizionario voti
Scrivi una funzione studenti_promossi(dizionario_voti) che prende in input un dizionario con {nome: voto}, e restituisce un elenco (lista) con i nomi degli studenti che hanno preso almeno 18.
'''

def studenti_promossi(dizionario_voti:dict[str: int]) -> list[str]:

    return [studente for studente, voti in dizionario_voti.items() if voti >= 18]

print(studenti_promossi({"Mario": 20, "Giovanni": 17, "Franco": 25, "Christian": 8}))