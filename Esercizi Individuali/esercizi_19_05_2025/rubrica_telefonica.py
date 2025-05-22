'''
1. Rubrica telefonica
Data una lista di tuple [(nome, numero)], costruisci un dizionario dove ogni nome è associato al numero.
'''


contatti = [("Luca", "3331234567"), ("Anna", "3927654321")]
# crea un dizionario rubrica da questa lista
rubrica:dict[str : str] = {}

for c in contatti:

    nome = c[0]
    numero = c[1]

    rubrica[nome] =  numero

print(rubrica)

'''
rubrica:dict[str : str ]= {}

for nome, numero in contatti:

    rubrica[nome] = numero

print(rubrica)

'''