max_posti:int = 100
nome_corso:str = input("Inserisci il nome del corso: ")

while True:

    opzione:str = input("Inserisci un'opzione: ")

    match opzione:

        case "iscrivi":

            if max_posti > 0:
               max_posti -= 1
            
            else:
                print("Non ci sono posti disponibili")

        case "annulla":

            if max_posti < 100:
                max_posti += 1

            else:
                print("Tutti i posti sono già disponibili")

        case "visualizza":

            print(max_posti)
            print(100 - max_posti)

        case "elimina":
            continue
        
        case "esci":
            break

        case _:
            print("Opzione inserita non valida")



        





