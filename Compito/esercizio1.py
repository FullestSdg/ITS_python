#Esercizio n.1
while True:
 parola:str = input("Inserire una parola: ")
 if parola == "fine" or parola == "FINE":
  break
 lettera_iniziale:str = parola[0]
 lettera_finale:str = parola[-1]

 if lettera_iniziale == lettera_finale:
     print(f"{parola} ha la stessa lettera iniziale e finale")

# soluzione:

while True:
    # Chiedo all'utente di inserire una parola da verificare
    parola:str = input("Inserire una parola per verificare se è palindroma: ").lower()

    # Controllo se l'utente ha inserito "fine" per terminare il programma
    if parola == "fine":
        break

    # Controllo se la parola è palindroma
    if parola == parola[::-1]:
        print("La parola è palindroma")
    # Se la parola non è palindroma
    else:
        print("La parola non è palindroma")
    