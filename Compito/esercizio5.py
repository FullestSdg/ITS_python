#Esercizio n.5
n:int = int(input("Inserire numero di euro disponibili: "))
if n == 0:
    print(f"Possiedi {n} euro")

numero_barrette:int = n 
coupon:int = n

while coupon >= 6:
    barrette_gratuite = coupon // 6
    numero_barrette += barrette_gratuite
    coupon = coupon % 6

print(f"Hai comprato {numero_barrette} barrette!")
print(f"Ti avanzano {coupon} coupon!")