# 1.1 Creare una funzione che preso in input un dizionario contenente come chiave una stringa (materia) e come valore una lista di nuneri (voti della materia) restituisca la media dei voti di ogni materio e ti dica qual è la materia in cui vai meglio.
# 1.2 Successivamente implementare un metodo che ti dica quanti voti ti servono per recuperare quella materia in caso sia insufficiente 

'''

def materia_media_voti(materie:dict[str : list[float]]) -> str:

    lista_media_voti:list[float] =[]
    dizionario_materie:dict[str: list[float]] = {}
    somma_voti = 0
    media_voti = 0
    materia_migliore = 0

    for materia, voti in materie.items():

        for v in voti:

            somma_voti += v

            media_voti += somma_voti / len(voti)

        if materia not in dizionario_materie:

            materie[materia] = lista_media_voti

            lista_media_voti.append(media_voti)

    for materia, voti in materie:

        if materie[voti] > materia_migliore:

            materia_migliore = materia

    return f"La materia migliore è {materia_migliore}\nQuesta invece è la media delle tue materie: {dizionario_materie}"

materie = {"italiano" : [8,7.5,6,9], "matematica" : [5,7,6.5], "scienze" : [10,8.5,7,9.5]}

risultato = materia_media_voti(materie = materie)
print(risultato)


'''

def materia_media_voti(materie: dict[str, list[float]]) -> str:
    
    dizionario_medie: dict[str, float] = {}
    materia_migliore = ""
    media_massima = 0

    for materia, voti in materie.items():

        if voti:

            media = sum(voti) / len(voti)
        
        dizionario_medie[materia] = media

        if media > media_massima:

            media_massima = media

            materia_migliore = materia

    return f"La materia migliore è '{materia_migliore}' con una media di {media_massima:.2f}\nMedie di tutte le materie: {dizionario_medie}"

materie = {"italiano" : [8,7.5,6,9], "matematica" : [5,7,6.5], "scienze" : [10,8.5,7,9.5]}
risultato = materia_media_voti(materie=materie)
print(risultato)


