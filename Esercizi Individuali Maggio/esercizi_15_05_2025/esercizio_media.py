# Crea una funzione calcola_media(lista) che riceve una lista di numeri e restituisce la loro media aritmetica.

def calcola_media(voti:list[float]) -> float:

    somma_voti = 0

    for v in voti:

        somma_voti += v 

    media_voti = somma_voti / len(voti)

    return float(media_voti)

media = calcola_media([4,8,7.5,10])
print(media)


