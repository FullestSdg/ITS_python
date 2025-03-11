n_tutor:int = 10
attesa:int = 0

while True:
    studente:str = input("Inserisci il tuo nome: ")

    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo")

    else:
        attesa += 1
        print("Studente in attesa")

    if n_tutor == 0 and attesa > 50:
        break
    
    else:
        continue