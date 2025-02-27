i = 0 #contatore ciclo while
contatore_testa:int = 0
contatore_croce:int = 0
percentuale_testa:int = 0
percentuale_croce:int = 0

while i < 8:
 
 coinflip:str = input("Lancio della moneta, digitare 't' o 'T' (testa) oppure 'c' o 'C' (croce): ")
 i += 1

 match coinflip:

    case "t"|"T":
        print("E' uscito Testa!")
        contatore_testa += 1
        print(f"Testa è uscita per {contatore_testa} volte")

        percentuale_testa = (contatore_testa * 100) / i
        print(f"Testa è uscita il {percentuale_testa:.2f}% delle volte")
    
    case "c"|"C":
        print("E' uscito Croce!")
        contatore_croce += 1
        print(f"Croce è uscita per {contatore_croce} volte ")

        percentuale_croce = (contatore_croce * 100) / i
        print(f"Croce è uscita il {percentuale_croce:.2f}% delle volte")