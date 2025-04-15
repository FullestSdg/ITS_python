'''
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.
'''

def somma_elementi(x: list[int], y: list[int]) -> list[int]:

    i = 0

    result:int[int] = []

    while i < len(x) and i < len(y):

      result.append(x[i]+y[i])

      i += 1
        
    return result

risultato = somma_elementi([2,3,3], [3,5,-3])
print(risultato)