posizione:int = int(input("Inserire un numero intero positivo: "))

if posizione > 3:
    print(f"{posizione}th")
elif posizione == 1:
    print(f"{posizione}st")
elif posizione == 2:
    print(f"{posizione}nd")
else:
    print(f"{posizione}rd")