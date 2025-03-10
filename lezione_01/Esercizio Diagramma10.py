r:float = float(input("Inserisci il tuo reddito: "))
m:float = float(input("Inserisci la media dei tuoi voti: "))

match r,m:

    case r,m if r < 20000 and m > 27:
        print("Borsa di studio approvata")
    
    case _:
        print("Borsa di studio rifiutata\nMotivo: Reddito o Media insufficiente")
