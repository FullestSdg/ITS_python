soglia:float = float(input("Inserire un numero soglia: "))

contatore = 0

while contatore != 7:
    n:float = float(input("Inserire un numero: "))
    contatore += 1

    if n > soglia:
      print(f"Il numero più grande è: {n}")
    
    else: 
       continue