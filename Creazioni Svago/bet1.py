import random

squadre:list[str] = ["Udinese", "Lazio", "Milan", "Inter", "Juventus", "Fiorentina", "Roma", "Genoa", "Sampdoria", "Napoli"]
lista1:list[int] = [0,1,2,3,4,5]
soldi:int = 100

while True:

    if soldi == 0:
        
        opzione3:str = input("Hai terminato i soldi, digita 'ricaricare' per rifornire il saldo oppure 'esci' per uscire: ")

        match opzione3:

            case "ricaricare":

                ricarica:int = int(input("Inserire un importo da aggiungere (centesimi non ammessi): "))

                soldi += ricarica
            
            case "esci":
                print("SEI STIRATO!!!!!!!!!!!")
                break

    opzione:str = input("Inserisci un'opzione tra gioca, visualizza, 'saldo disponibile' ed esci : ").lower()

    match opzione:

        case "visualizza":

            squadra_casuale1 = random.sample(squadre,1)[0]
            squadra_casuale2 = random.sample(squadre,1)[0]

            if squadra_casuale1 == squadra_casuale2:

                squadra_casuale1 = random.sample(squadre,1)[0]
                squadra_casuale2 = random.sample(squadre,1)[0]

            print(f"Partita tra {squadra_casuale1} : {squadra_casuale2}")

            opzione2:str = input("Inserisci un'opzione tra gioca o skippa : ").lower()

            match opzione2:

                case "skippa":

                    print("Partita saltata, sei na pussy")
                    pass

                case "gioca":

                    pronostico:str = input("Inserisci il tuo pronostico secondo questi criteri '0' - '0': ")

                    reti_casa = random.sample(lista1,1)[0]
                    reti_ospite = random.sample(lista1,1)[0]
                    risultato = f"{reti_casa} - {reti_ospite}"

                    if risultato == pronostico:

                        soldi += 20
                        print(risultato)
                        print("Congratulazioni, hai vinto la bet!")
                    
                    else:
                        soldi -= 10
                        print(risultato)
                        print("Peccato hai perso la bet!")

                case _:

                    print("Opzione inserita non valida")
                    continue
        
        case "gioca":
                                
            pronostico:str = input("Inserisci il tuo pronostico secondo questi criteri '0' - '0': ")

            squadra_casuale1 = random.sample(squadre,1)[0]
            squadra_casuale2 = random.sample(squadre,1)[0]

            if squadra_casuale1 == squadra_casuale2:

                squadra_casuale1 = random.sample(squadre,1)[0]
                squadra_casuale2 = random.sample(squadre,1)[0]

            print(f"Partita tra {squadra_casuale1} : {squadra_casuale2}")

        
            reti_casa = random.sample(lista1,1)[0]
            reti_ospite = random.sample(lista1,1)[0]
            risultato = f"{reti_casa} - {reti_ospite}"

            if risultato == pronostico:

                soldi += 20
                print(risultato)
                print("Congratulazioni, hai vinto la bet!\n CASSAAAAAAAAAAAAAAAAAA!!!!!!!!")
                    
            else:
                soldi -= 10
                print(risultato)
                print("Peccato hai perso la bet!")

        case "saldo disponibile":

            print(f"Questo è il tuo saldo: {soldi}")

        case "esci":
            print("Sei uscito dalla sala scommesse, pussy")
            break

        case _:
            print("Opzione inserita non valida")