soldi:int = int(input("Inserisci un importo: "))

match soldi:

    case soldi if soldi >= 4:
        print("Andiamo all'elementare")
    
    case _:
        print("Semo stirati\nMa ci andremo lo stesso (si paga con la carta)")