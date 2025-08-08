from Rep3_S_DeGuidi import *

# Inizializzazione
alieno1 = Alieno("Robot")
mostro1 = Mostro("gOrThOr", "ESDRONGO", "ESDRANGO")

print(alieno1)
print("Munizioni:", alieno1.getMunizioni())

print()
print(mostro1)
print("Assalto:", mostro1.getAssalto())

# Combattimento
vincitore = combattimento(alieno1, mostro1)

# Proclamazione
if vincitore:
    if isinstance(vincitore, Alieno):
        print("\nGli Alieni hanno vinto!")
    else:
        print("\nI Mostri hanno vinto!")
    proclamaVincitore(vincitore)