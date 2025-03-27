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

    opzione:str = input("Inserisci un'opzione tra visualizza, 'saldo disponibile' ed esci : ").lower()

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

                    scommessa:str = input("Cosa vuoi scommettere tra: somma goal, risultato esatto, over/under, goal/nogoal: ")

                    reti_casa = random.sample(lista1,1)[0]
                    reti_ospite = random.sample(lista1,1)[0]
                    risultato = f"{reti_casa} - {reti_ospite}"

                    match scommessa:

                        case "somma goal":

                            somma_goal:int = int(input("Inserisci un numero (massimo 10), che rappresenterà la somma dei goal: "))

                            if somma_goal > 10:
                                print("Errore numero inserito non valido")

                            if reti_casa + reti_ospite == somma_goal:
                                soldi += 20
                                print(risultato)
                                print(f"Congratulazioni! {somma_goal} era il numero esatto!\n CASSAAAAAAAAA!!!")
                            
                            else:
                                soldi -= 10
                                print(risultato)
                                print(f"Peccato hai perso! {reti_casa + reti_ospite} era il numero corretto")
                        
                        case "risultato esatto":

                            pronostico:str = input("Inserisci quello che secondo te sarà il risultato esatto, usa questo criterio ('0' - '0'): ")

                            if pronostico == risultato:
                                soldi += 20
                                print(risultato)
                                print(f"Congratulazioni! Hai fatto cassaaaaaaaaaaaaaaa!!")

                            else:
                                soldi -= 10
                                print(risultato)
                                print(f"Peccato hai perso! Andrà meglio la prossima :)")
                        
                        case "over/under":

                            over_under_utente:str = input("Inserisci un'opzione tra over, under, x-over, x-under: ")

                            match over_under_utente:

                                case "over":

                                    over:float = float(input("Inserisci un valore tra '1.5','2.5','3.5','4.5': "))

                                    if reti_casa + reti_ospite > over:

                                        if over == 1.5:
                                            soldi += 10
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati ridati 10€ !")
                                        
                                        elif over == 2.5:
                                            soldi += 15
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 15€ !")
                                        
                                        elif over == 3.5:
                                            soldi += 20
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 20€ !")
                                        
                                        else:
                                            soldi += 25
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 25€ !\nCASSA GROSSA!!!")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")
                                    
                                case "under": 

                                    under:float = float(input("Inserisci un valore tra '1.5','2.5','3.5','4.5': "))

                                    if reti_casa + reti_ospite < under:

                                        if under == 1.5:
                                            soldi += 25
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 25€ !\nCASSA GROSSA!!!")
                                        
                                        elif under == 2.5:
                                            soldi += 20
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 20€ !")
                                        
                                        elif under == 3.5:
                                            soldi += 15
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 15€ !")
                                        
                                        else:
                                            soldi += 10
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati ridati 10€ !")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")

                                case "x-over": 

                                    x_over:float = float(input("Inserisci un valore tra '1.5','3.5','5.5': "))

                                    if reti_casa + reti_ospite > x_over and reti_casa == reti_ospite:

                                        if x_over == 1.5:
                                            soldi += 20
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati ridati 20€ !")
                                        
                                        elif x_over == 3.5:
                                            soldi += 25
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 25€ !")
                                        
                                        else:
                                            soldi += 35
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 35€ !\nCASSA GROSSA!!!")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")
                                
                                case "x-under": 

                                    x_under:float = float(input("Inserisci un valore tra '1.5','3.5','5.5': "))

                                    if reti_casa + reti_ospite > x_under and reti_casa == reti_ospite:

                                        if x_under == 5.5:
                                            soldi += 20
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati ridati 20€ !")
                                        
                                        elif x_under == 3.5:
                                            soldi += 25
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 25€ !")
                                        
                                        else:
                                            soldi += 35
                                            print(risultato)
                                            print("Congratulazioni hai vinto! Ti sono stati dati 35€ !\nCASSA GROSSA!!!")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")
                   
                        case "goal/nogoal":

                            goal_nogoal_utente:str = input("Inserisci un'opzione tra 'goal','nogoal','1-goal','2-goal','x-goal': ")

                            match goal_nogoal_utente:

                                case "goal":

                                    if reti_casa and reti_ospite >= 1:
                                        soldi += 20
                                        print(risultato)
                                        print("Congratulazioni hai vinto!\nHai guadagnato 20€")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")
                                
                                case "nogoal":

                                    if reti_casa or reti_ospite == 0:
                                        soldi += 20
                                        print(risultato)
                                        print("Congratulazioni hai vinto!\nHai guadagnato 20€")
                                    
                                    else:
                                        soldi -= 10
                                        print(risultato)
                                        print("Peccato hai perso!")
                                
                                case "1-goal":

                                    if reti_casa >= 1 and reti_ospite >= 1 and reti_ospite < reti_casa:
                                        soldi += 30
                                        print(risultato)
                                        print("Congratulazioni hai vinto!\nHai guadagnato 30€\nCASSAAAAAAAAAAAAAAAAA!!!!")
                                
                                case "2-goal":

                                    if reti_casa >= 1 and reti_ospite >= 1 and reti_ospite > reti_casa:
                                        soldi += 30
                                        print(risultato)
                                        print("Congratulazioni hai vinto!\nHai guadagnato 30€\nCASSAAAAAAAAAAAAAAAAA!!!!")
                                
                                case "x-goal":

                                    if reti_casa >= 1 and reti_ospite >= 1 and reti_ospite == reti_casa:                                       
                                        soldi += 40
                                        print(risultato)
                                        print("Congratulazioni hai vinto!\nHai guadagnato 40€\nCASSAAAAAAAAAAAAAAAAA!!!!")

                case _:

                    print("Opzione inserita non valida")
                    continue

        case "saldo disponibile":

            print(f"Questo è il tuo saldo: {soldi}")

        case "esci":
            print("Sei uscito dalla sala scommesse, pussy")
            break

        case _:
            print("Opzione inserita non valida")