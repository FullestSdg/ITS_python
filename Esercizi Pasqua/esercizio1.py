def transform(x: int) -> int:
    valore_trasformato = 0
    
    if x % 2 == 0:
        valore_trasformato = x / 2
    
    elif x % 2 == 1:
        valore_trasformato = (x * 3) - 1

    return valore_trasformato

risultato = transform(7)
print(risultato)
            
