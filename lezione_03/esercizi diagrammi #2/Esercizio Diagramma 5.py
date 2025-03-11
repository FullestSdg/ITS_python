n:int = int(input("Inserisci un numero: "))

if n % 1 == 0 and n > 0:

    sum = 0
    i = 1

    while True: 
    
       if i > n:
          
          print(sum)
          break
          

       else:
          sum += i * i
          i += 1
else:
   print(f"Errore {n} deve essere positivo")
      
    


   

    


