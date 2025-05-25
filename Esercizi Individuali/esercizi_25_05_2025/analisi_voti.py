'''
🟢 Esercizio 5: Analisi su dizionario di voti
Scrivi una funzione analizza_voti(voti_dict) che:

Riceve un dizionario con i nomi degli studenti come chiavi e i voti come valori

Restituisce:

La media dei voti

La lista degli studenti che hanno ottenuto più della media
'''

def analizza_voti(voti_dict:dict[str : float]) -> float:

    studenti_più_della_media:list[str] = []
    somma_voti = 0

    for studente, voto in voti_dict.items():

        somma_voti += voto

    media = somma_voti / len(voti_dict)

    for studente, voto in voti_dict.items():
        
        if voto > media:

            studenti_più_della_media.append(studente)

    return studenti_più_della_media

print(analizza_voti({"Giuseppe": 8.5, "Mario": 5, "Francesco": 6, "Antonio": 10, "Giovanni": 7.5}))