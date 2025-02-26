#Esercizio n.10

lista_numeri:list = []
somma_pari:int = 0
somma_dispari:int = 0
media:int = 0
contatore_dispari:int = 0
lista_frequenza:list = []
frequenza:int = 0

while True:
    numeri:int = int(input("Inserire un numero intero (digitare 0 per terminare): "))

    if numeri == 0:
     break

    lista_numeri.append(numeri)
    
    if numeri % 2 == 0:
        somma_pari += numeri
    print(f"La somma attuale dei numeri pari è: {somma_pari}")
    
    if numeri % 2 == 1:
        contatore_dispari += 1
        somma_dispari += numeri
        media = somma_dispari / contatore_dispari
    print(f"La media attuale dei numeri dispari è: {media}")
    
    for i in lista_numeri:
     contatore = lista_numeri.count(i) #contatore = contatore frequenza

    if contatore > frequenza:
        frequenza = contatore #contatore = contatore frequenza
        lista_frequenza = [i]
    
    elif contatore == frequenza and i not in lista_frequenza: #contatore = contatore frequenza
       
        lista_frequenza.append(i)

    for i in lista_frequenza:
      print(f"Il numero più frequente è: {i} (Con {frequenza} volte)")



