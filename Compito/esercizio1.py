#Esercizio n.1
while True:
 parola:str = input("Inserire una parola: ")
 if parola == "fine" or parola == "FINE":
  break
 lettera_iniziale:str = parola[0]
 lettera_finale:str = parola[-1]

 if lettera_iniziale == lettera_finale:
     print(f"{parola} ha la stessa lettera iniziale e finale")
