#Esercizio n.8
n = 0
while n < 5:
    numeri = int(input("Inserire un numero intero compreso tra 1 e 30: "))
    n += 1
    
    if numeri < 1 or numeri > 30:
        print("Numero inserito non valido")
        break

    for i in range(numeri + 1):
       asterischi = i * "*"
    print(asterischi)





