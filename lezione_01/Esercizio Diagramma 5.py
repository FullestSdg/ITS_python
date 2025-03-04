n:int = int(input("Inserire un numero: "))

if n < 2:
    print(f"{n} non è primo")

DIV:int = 2
primo = True

while True:
 
 if DIV < n:
    if n % DIV == 0:
        print(f"{n} non è primo")
    
    else:
        DIV += 1
        n = primo

else:
     print(f"{n} è primo")