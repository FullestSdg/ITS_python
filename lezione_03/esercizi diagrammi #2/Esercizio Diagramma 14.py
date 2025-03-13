punteggio:int = 0

while punteggio < 100:

       D1:int = int(input("Inserisci un numero tra 1 a 6: "))
       D2:int = int(input("Inserisci un numero tra 1 a 6: "))

       if D1 > 0 and D1 <= 6 and D2 > 0 and D2 <= 6:
           
           sum = D1 + D2

           if D1 % 2 == 0 and D2 % 2 == 0 and sum > 8:
               
               punteggio == 100
               break

           elif D1 == 6 or D2 == 6 or sum == 7:
               
               punteggio += 10

           else:
               punteggio = 0
               print("Sconfitta")
               break
        
       else:
           print("Numeri inseriti non validi")
           continue

           
        