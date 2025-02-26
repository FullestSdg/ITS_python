nome:str = input("Inserire il tuo nome: ")
ruolo:str = input("Inserire il tuo ruolo: ")
età:int = int(input("Inserire la tua età: "))

dizionario_sdrogo:dict = {"nome" : nome, "ruolo" : ruolo, "età": età}

match ruolo:

    case "admin":
        print("Accesso a tutte le funzionalità")

    case "moderatore":
        print("Puoi gestire i contenuti ma non modificare le impostazion")
    
    case "utente":
         if età >= 18:
             print("Accesso standard a tutti i servizi")
         else:
             print("Accesso limitato! Alcune funzionalità sono bloccate.")

    case "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")