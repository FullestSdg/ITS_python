

def baricentro(v:list[int]) -> int | None:

    somma_totale = sum(v)
    somma_iniziale = 0

    for numeri in range(len(v)):

        somma_iniziale += v[numeri]
        somma_finale = somma_totale - somma_iniziale

        if somma_iniziale == somma_finale:

            return numeri
        
    return None

print(baricentro([1,2,3,4,1,1]))