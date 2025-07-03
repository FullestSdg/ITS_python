import math
from typing import Any
    
def calculateChanges(numero_ore: float | int) -> str:

    costo = 2

    if numero_ore > 3 and numero_ore < 24:

        costo += 0.5 * (math.floor(numero_ore) - 3)

        return costo

    elif numero_ore >= 24:

        costo = 10

        costo += 0.5 * (math.floor(numero_ore)- 24)
            
        return costo

    else:

        return costo


print(f"{'Car':<10} {'Hours':<10} {'Charge':<10}")

clienti:list[Any] = [1.5,4.0,5.50,24.0]
total = 0

for item in clienti:

    c = calculateChanges(item)
    total += c

    print(f"{clienti.index(item)+1:<10} {item:<10} {total:.2f}$")

print(f"{'TOTAL':<10} {sum(clienti):<10} {total:.2f}$")


