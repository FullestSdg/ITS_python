day:int = int(input("Inserire un giorno: "))
month:int = int(input("Inserire un mese: "))

festività:tuple = (day, month)

match festività:

    case (1, 1):
        print(f"Il {festività[0]}/{festività[1]} è Capodanno!")
    
    case (14, 2):
        print(f"Il {festività[0]}/{festività[1]} è San Valentino!")
    
    case (2, 6):
        print(f"Il {festività[0]}/{festività[1]} è la Festa Della Repubblica")
    
    case (15, 8):
        print(f"Il {festività[0]}/{festività[1]} è Ferragosto")

    case (31, 10):
        print(f"Il {festività[0]}/{festività[1]} è Halloween!")

    case (25, 12):
        print(f"Il {festività[0]}/{festività[1]} è Natale!")
    
    case _:

        if day > 31 or  day < 1:  # fatto per diletto
           print("Errore numero inserito non valido")
        elif month == 2 and day == (30,31):  # fatto per diletto
           print(f"Errore {month} non ha 30 e 31 giorni!")
        elif month > 12 or month < 1: # fatto per diletto
           print("Errore numero inserito non valido")
        else:
           print("Nessuna festività in questa data")