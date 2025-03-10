max_posti:int = 100

while True:

    nome_corso:str = input("Inserisci il nome del corso: ")

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
                print("Tutti i posti sono igà disponibili")

        case "visualizza":

            print(max_posti)
            print(100 - max_posti)

        case "elimina":
            

        





