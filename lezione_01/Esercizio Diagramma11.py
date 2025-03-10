posti:int = 20

while True:
 
 opzione:str = input("Inserire un opzione: ").strip().lower()

 match opzione:

    case "prenota":

        if posti > 0:
         posti -= 1
        
        else:
            print("Non ci sono posti disponibili")

    case "libera":
      
        if posti < 20:
          posti += 1

        else:
           print("Tutti i posti sono già disponibili")

    case "visualizza":
      
      print(f"I posti liberi sono {posti}")
      print(f"I posti occupati sono {20 - posti}")

    case "esci":
      print("Sei uscito dal sistema")
      break

    case _:
       print(f"{opzione} non è un'opzione valida")