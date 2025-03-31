import random

numeri_casuali:list[int] = [1,2,3,4,5,6,7,8,9,10]

percorso:list[int] = []

for i in range(71):
    percorso.append("_")

print(*percorso)
percorso_singolo = percorso[0]
print(*percorso_singolo)


def mosse_tartaruga():

    mossa:int = random.sample(numeri_casuali,1)

    match mossa:

        case mossa if mossa >= 1 and mossa <= 5:

            print("Tartaruga esegue scivolata ")