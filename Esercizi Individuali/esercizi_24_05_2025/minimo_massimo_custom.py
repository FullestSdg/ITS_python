'''
🔴 Esercizio 4 – Minimo e massimo personalizzato
Scrivi una funzione trova_estremi(lista, tipo="entrambi") che:

Ritorna:

solo il minimo se tipo="min"

solo il massimo se tipo="max"

entrambi (in una tupla) se tipo="entrambi"

Gestisci anche il caso in cui la lista sia vuota (ritorna None o messaggio)
'''

def trova_estremi(lista:list[int], tipo="entrambi") -> int | tuple[int]:

    minimo = 0
    massimo = 0

    for numbers in lista:

        match tipo:

            case tipo if tipo == "max":

                if massimo > numbers:

                    numbers == massimo
                    return massimo
            
            case tipo if tipo == "min":

                if minimo < numbers:

                    numbers == minimo
                    return minimo
            
            case tipo if tipo == "entrambi":

                if massimo > numbers:

                    numbers == massimo
                
                elif minimo < numbers:

                    numbers == minimo

                return (massimo, minimo)
            
print(trova_estremi([1,2,3,4,5,6,7], "entrambi"))