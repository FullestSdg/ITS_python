#Esercizio m.2
frase:str = input("Inserire una frase: ")

if frase.count(' ') == 1:
    print("La frase ha un solo spazio")
else:
    print(f"La frase digitata ha {frase.count(' ')} spazi")


