sergio_numeri:list = [20,92]
alessandro_numeri:list = [17,76]
giuseppe_numeri:list = [46,54]
daniel_numeri:list = [69,104]
daniele_numeri:list = [104,69]

numeri: dict = {"Sergio": sergio_numeri , "Alessandro": alessandro_numeri , "Giuseppe": giuseppe_numeri, "Daniel": daniel_numeri, "Daniele": daniele_numeri}

'''numero1 = numeri["Sergio"]
print("Sergio",numero1)

numero2 = numeri["Alessandro"]
print("Alessandro",numero2)

numero3 = numeri["Giuseppe"]
print("Giuseppe",numero3)

numero4 = numeri["Daniel"]
print("Daniel",numero4)

numero5 = numeri["Daniele"]
print("Daniele",numero5)'''

# Con ciclo for 

for nome, numeri_persona in numeri.items():
    print(f"Numeri preferiti da {nome}: ") #, "{",'; '.join([str(x) for x in numeri_persona]), "}")

    # stampare i numeri preferiti dalla persona, uno per riga
    
    for n in numeri_persona:
        print(f"\t{n}")
