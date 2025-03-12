contatore:int = 0
sum:int = 0

while True:
   
   scelta:str = input("Inserire una scelta: ").lower()
   
   match scelta:

    case "si":

        voto:float = float(input("Inserisci il tuo voto: "))

        if voto > 0:
            contatore += 1
            sum = sum + voto 
        
        else:
            print(f"Errore, {voto} non è un voto valido")
            
    case "no":

        if contatore > 0:
            media = sum / contatore
            print(media)
            break

        else:
            print("Errore nessun voto inserito")

    case _:
           print(f"Errore {scelta} non è una scelta valida")

    
