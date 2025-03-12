età:int = int(input("Inserire un'età: "))

match età:

    case età if età >= 18 and età <= 65:
        print("Puoi partecipare all'attività")
    
    case età if età < 18:
        print("Non puoi partecipare all'attività, non hai l'età minima richiesta!")

    case _:
        print("Non puoi partecipare all'attività, hai superato l'età massima consentita!")