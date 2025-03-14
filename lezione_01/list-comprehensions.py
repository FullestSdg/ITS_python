'''lista_1 = [ i for i in range(10)]
dict_1 = { i : i for i in range (10)}

print(f"{lista_1}\n{dict_1}")


lista_2 = ["a", "b", "c"]
for idx, char in enumerate(lista_2):
    lista_2[idx] = char.upper()

print(lista_2)
'''

import random

squadre:list[str] = ["Udinese", "Lazio", "Milan", "Inter", "Juventus", "Fiorentina", "Roma", "Genoa", "Sampdoria", "Napoli"]
lista1:list[int] = [0,1,2,3,4,5]
soldi:int = 10

while True:

    opzione:str = input("Inserisci un'opzione tra gioca ed esci : ").lower()

    match opzione:

        case "visualizza":

            squadra_casuale1 = random.sample(squadre,1)
            squadra_casuale2 = random.sample(squadre,1)
            print(f"Partita tra {squadra_casuale1} : {squadra_casuale2}")


            


