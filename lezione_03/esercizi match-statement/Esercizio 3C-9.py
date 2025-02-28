x:int = int(input("Inserire un valore di x: "))
y:int = int(input("Inserire un valore di y: "))

punto:tuple  = (x, y)

match punto:
    
    case (0, 0):
        print(f"Il punto {punto} si trova sull'origine")

    case (x, 0):
        print(f"Il punto {punto} si trova sull'asse delle x")
    
    case (0, y):
        print(f"Il punto {punto} si trova sull'asse delle y")

    case (x, y):

        if x > 0 and y > 0:
            print(f"Il punto {punto} si trova nel primo quadrante")
        elif x < 0 and y > 0:
            print(f"Il punto {punto} si trova nel secondo quadrante")
        elif  x < 0 and y < 0:
            print(f"Il punto {punto} si trova nel terzo quadrante")
        else:
            print(f"Il punto {punto} si trova nel quarto quadrante")