a:int = float(input("Inserire un numero: "))
b:int = float(input("Inserire un numero: "))

if a > b:
    c = (a**2 - b**2)**0.5
    print(f"Il valore di c è:{c}")

else:
    print("Errore")