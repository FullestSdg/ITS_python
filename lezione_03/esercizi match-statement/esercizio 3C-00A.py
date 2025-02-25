bambini:int = int(input("Inserire un numero intero positivo: "))

match bambini:

 case 1:
  print("Congratulazioni")

 case 2:
  print("Wow, Gemelli!")

 case 3:
  print("Wow, Tre!")

 case 4:
  print("Mamma mia, Quattro wow!")

 case 5: 
  print("Wow incredibile, cinque!")

 case _:
  print(f"Non ci credo! {bambini} bambini!")


