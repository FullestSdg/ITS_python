'''
4. Unione di voti
Hai due dizionari:
'''

voti1 = {"Mario": 28, "Luca": 24}
voti2 = {"Luca": 30, "Giulia": 27}

# Crea un nuovo dizionario con la media dei voti se lo studente compare in entrambi, altrimenti prendi il voto presente.

voti3 = voti1 | voti2

for nome, voto in voti3.items():

    if nome in voti1 and voti2:

        media = voto / 2

        media_studente:dict[str : float] = {}

        media_studente[nome] = media

print(media_studente)


