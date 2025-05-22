'''
4. Unione di voti
Hai due dizionari:
'''

voti1 = {"Mario": 28, "Luca": 24}
voti2 = {"Luca": 30, "Giulia": 27}

# Crea un nuovo dizionario con la media dei voti se lo studente compare in entrambi, altrimenti prendi il voto presente.

voti_totali = {}
studenti = set(voti1.keys()).union(voti2.keys())

for studente in studenti:

    if studente in voti1 and studente in voti2:

        voti_totali[studente] = (voti1[studente] + voti2[studente]) // 2

    elif studente in voti1:

        voti_totali[studente] = voti1[studente]

    else:

        voti_totali[studente] = voti2[studente]

print(voti_totali)




